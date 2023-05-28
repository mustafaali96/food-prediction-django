from rest_framework.generics import ListAPIView
from revoke_app.serializers import FoodCategorySerializer
from revoke_app import models


class FoodCategoryAPIView(ListAPIView):
    queryset = models.FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer