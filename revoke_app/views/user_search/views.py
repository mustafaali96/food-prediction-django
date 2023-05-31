from rest_framework.generics import ListAPIView
from revoke_app.serializers import UserSearchSerializer
from revoke_app.serializers import DishSerializer
from revoke_app import models
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
        dishes = models.Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

