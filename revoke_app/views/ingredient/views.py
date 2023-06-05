from rest_framework.generics import ListAPIView
from revoke_app.serializers import IngredientSerializer
from revoke_app import models
# from django.db.models.functions import Min
from django.db.models import Min


class IngredientAPIView(ListAPIView):
    # queryset = models.Ingredient.objects.all()
    queryset = models.Ingredient.objects.filter(
                        id__in=models.Ingredient.objects.values('ingredient').annotate(
                        min_id=Min('id')).values('min_id')).values('id', 'ingredient')
    serializer_class = IngredientSerializer
