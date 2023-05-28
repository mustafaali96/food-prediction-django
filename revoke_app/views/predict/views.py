from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from rest_framework.permissions import IsAuthenticated

from revoke_app.serializers import PredictFoodSerializer

import json
import os


class PredictFoodAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PredictFoodSerializer

    def post(self, request, *args, **kwargs):

        serializer_validation = self.serializer_class(data=request.data)

        if serializer_validation.is_valid():
            file_path = os.path.join(settings.BASE_DIR, 'db-recipes.json')

            # Read the contents of the file
            with open(file_path, 'r') as file:
                json_data = file.read()

            # Deserialize the JSON data
            data = json.loads(json_data)
            return Response(data)
        
        return Response(serializer_validation.errors, status=status.HTTP_400_BAD_REQUEST)
