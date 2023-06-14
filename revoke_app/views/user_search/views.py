from rest_framework.generics import ListAPIView
from revoke_app.serializers import UserSearchSerializer
from revoke_app.serializers import DishSerializer
from revoke_app import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import pickle
import numpy as np
# from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier
from RevokeProject.settings.base import BASE_DIR
import os


class UserSearchAPIView(ListAPIView):
    queryset = models.UserSearch.objects.all()
    serializer_class = UserSearchSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            # Perform the search based on user_id
            queryset = self.queryset.filter(user=user_id)
            return queryset
        return super().get_queryset()
    
@api_view(['POST'])
def create_user_search_data(request):
    serializer = UserSearchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # ML Code
        modelPath = os.path.join(BASE_DIR, "ai_model/finalized_model.sav")
        loaded_model = pickle.load(open(modelPath, 'rb')) 
        featureLst = loaded_model.feature_names_in_
        Ingredient = request.POST.getlist('Ingredient')
        IngredientQueryset = models.Ingredient.objects.filter(id__in=Ingredient)
        IngredientLst = list(IngredientQueryset.values_list('ingredient', flat=True))
        predictLst = []
        for feature in featureLst:
            if feature in IngredientLst:
                predictLst.append(1)
            else:
                predictLst.append(0)
        predictLst[0] = request.data['category']
        predictLst[1] = request.data['foodCategory']
        probLst = loaded_model.predict_proba([predictLst])[0]
        classIdxs = sorted(
                        range(len(probLst)),
                        key=lambda index: probLst[index])
        predictClasses = [loaded_model.classes_[i] for i in classIdxs[:10]] # top 10 predictions
        dishes = models.Dish.objects.filter(name__in=predictClasses)
        ordered_queryset = sorted(dishes, key=lambda obj: predictClasses.index(obj.name))
        serializer = DishSerializer(ordered_queryset, many=True)

        # extra filters

        userId = request.data['user']
        userData = models.User.objects.filter(id=userId).first()
        userBp = userData.bp
        userSugar = userData.sugar
        mostRec = {}
        dishesList = models.Dish.objects.all() 
        for dish in dishesList:
            unHealthy = False
            mostRec[dish.name] = 0
            for ingredient in IngredientLst:
                if dish.Ingredient.filter(ingredient=ingredient).exists():
                    mostRec[dish.name] += 1
            if dish.category.filter(id=request.data['category']).exists():
                mostRec[dish.name] += 1
            if dish.foodCategory.id == int(request.data['foodCategory']):
                mostRec[dish.name] += 1
            if userSugar != 'Normal' and dish.foodCategory.foodCategory in ['Desert']:
                del mostRec[dish.name]
                unHealthy = True
            if unHealthy:
                continue
            for dishIngredient in models.Dish.objects.filter(name=dish.name):
                dishIngredient = [f.ingredient for f in dishIngredient.Ingredient.all()]
            for ingredient in dishIngredient:
                if unHealthy:
                    continue
                if userBp != 'Healthy' and ingredient.lower() in ['butter', 'oil', 'ghee', 'cottage cheese', 'mozzarella cheese', 'paratha']:  # high bp ingredients
                    del mostRec[dish.name]
                    unHealthy = True
                if userSugar != 'Normal' and ingredient.lower() in ['sugar'] and not unHealthy:
                    del mostRec[dish.name]
                    unHealthy = True
            
        
        mostRecClasses = sorted(mostRec.items(), key=lambda x:x[1], reverse=True)
        mostRecClassesDict = dict(mostRecClasses)
        mostRecClassesDict = dict((k, v) for k, v in mostRecClassesDict.items() if v > 0)
        predictClasses = list(mostRecClassesDict.keys())
        dishes = models.Dish.objects.filter(name__in=predictClasses)
        ordered_queryset = sorted(dishes, key=lambda obj: predictClasses.index(obj.name))
        serializer = DishSerializer(ordered_queryset, many=True)

        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def create_user_search_model(request):
    # ML Code
    # Train mode
    df = pd.DataFrame(list(models.Dish.objects.all().values('name', 'category', 'foodCategory', 'Ingredient__ingredient')))
    df.rename(columns = {'Ingredient__ingredient':'ingredient'}, inplace = True)
    df['ingredient'] = df['ingredient'].apply(lambda x:x.lower())
    df['value'] = 1
    df = np.round(pd.pivot_table(df, values='value',
                            index=['name', 'category', 'foodCategory'], 
                            columns= 'ingredient', 
                            aggfunc=np.mean,
                            fill_value=0),2)
    df.reset_index(inplace=True)
    df.columns.name = None
    X = df.loc[:, df.columns!='name']
    y = df["name"]
    # clf = DecisionTreeClassifier()
    clf = RandomForestClassifier(max_depth=10, random_state=0)
    # Train Random Forest Classifer
    clf = clf.fit(X,y)
    # save model
    modelPath = os.path.join(BASE_DIR, "ai_model/finalized_model.sav")
    pickle.dump(clf, open(modelPath, 'wb'))
    return Response(status=200)