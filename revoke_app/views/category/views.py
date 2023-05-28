from rest_framework.generics import ListAPIView
from revoke_app.serializers import CategorySerializer
from revoke_app import models


class CategoryAPIView(ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer