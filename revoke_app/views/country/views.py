from rest_framework.generics import ListAPIView
from revoke_app.serializers import CountrySerializer
from revoke_app import models


class CountryAPIView(ListAPIView):
    queryset = models.Country.objects.all()
    serializer_class = CountrySerializer
