from rest_framework.generics import ListAPIView
from revoke_app.serializers import DishSerializer
from revoke_app import models


class DishAPIView(ListAPIView):
    queryset = models.Dish.objects.all()
    serializer_class = DishSerializer
