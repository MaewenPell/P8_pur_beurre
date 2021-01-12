from django.contrib import admin
from .models import Aliment, Category, Favorite


admin.site.register([Aliment, Favorite, Category])
