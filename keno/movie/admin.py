from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class ProductAdmin(admin.ModelAdmin):
    pass
