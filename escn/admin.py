from django.contrib import admin
from .models import State , RelationShip , Gender
# Register your models here.
admin.site.register(Gender)
admin.site.register(RelationShip)
admin.site.register(State)
