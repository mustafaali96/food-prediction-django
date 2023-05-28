# Framework imports
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, ListModelMixin
from django.contrib.auth import get_user_model

# App level imports
from revoke_app.serializers import RegisterUserSerializer


class UserSignUpCreateView(RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    model = get_user_model()
    queryset = get_user_model().objects.filter(is_admin=False)
    serializer_class = RegisterUserSerializer



