from django.views.generic import View
from revoke_app.core.custom_mixins import CustomLoginAndMenuValidatorMixin


class BaseViewForAuthenticatedClass(CustomLoginAndMenuValidatorMixin, View):
    
    def get(self, request, *args, **kwargs):
        raise NotImplementedError("get method not implemented.")
    
    def post(self, request, *args, **kwargs):
        raise NotImplementedError("post method not implemented.")
    
    def put(self, request, *args, **kwargs):
        raise NotImplementedError("put method not implemented.")
    
    def patch(self, request, *args, **kwargs):
        raise NotImplementedError("patch method not implemented.")
    
    def delete(self, request, *args, **kwargs):
        raise NotImplementedError("delete method not implemented.")

