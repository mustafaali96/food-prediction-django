from django.contrib import admin

from revoke_app.models import *
from revoke_app.models.recipes import *

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Ingredient)
admin.site.register(Dish)


