from django.contrib import admin

# Register your models here.

from .models import Animal, Tag

admin.site.register(Animal)
admin.site.register(Tag)
