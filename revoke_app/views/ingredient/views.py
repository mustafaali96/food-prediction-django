from rest_framework.generics import ListAPIView
from revoke_app.serializers import IngredientSerializer
from revoke_app import models


class IngredientAPIView(ListAPIView):
    queryset = models.Ingredient.objects.all()
    serializer_class = IngredientSerializer
