from django.contrib import admin
from .models import Aliment, User, Category


admin.site.register([Aliment, User, Category])