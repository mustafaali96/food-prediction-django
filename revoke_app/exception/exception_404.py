# Framewrok imports
from django.views.decorators.csrf import requires_csrf_token
from django.http import JsonResponse
from django.views.defaults import page_not_found

# Rest framework imports
from rest_framework import status


@requires_csrf_token
def custom_page_not_found(request, exception, template_name=None):

  exception_repr = exception.__class__.__name__

  if exception_repr != "Resolver404":
    return page_not_found(request, exception)
 
  context = {
      'message': "The path you've requested doesn't exists",
  }
  return JsonResponse(data=context, status=status.HTTP_404_NOT_FOUND)