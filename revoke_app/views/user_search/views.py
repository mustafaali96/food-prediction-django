from rest_framework.generics import ListAPIView
from revoke_app.serializers import UserSearchSerializer
from revoke_app.serializers import DishSerializer
from revoke_app import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import pickle
import numpy as np
from sklearn.tree import DecisionTreeClassifier 
from RevokeProject.settings.base import BASE_DIR


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
        loaded_model = pickle.load(open("ai_model/finalized_model.sav", 'rb')) 
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
        dishes = models.Dish.objects.filter(name=loaded_model.predict([predictLst])[0])
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def create_user_search_model(request):
    # ML Code
    # Train mode
    df = pd.DataFrame(list(models.Dish.objects.all().values('name', 'category', 'foodCategory', 'Ingredient__ingredient')))
    df.rename(columns = {'Ingredient__ingredient':'ingredient'}, inplace = True)
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
    clf = DecisionTreeClassifier()
    # Train Decision Tree Classifer
    clf = clf.fit(X,y)
    # save model
    filename = 'ai_model/finalized_model.sav'
    pickle.dump(clf, open(filename, 'wb'))
    return Response(status=200)