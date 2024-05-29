from django.contrib import admin
from .models import User, Products

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'country', 'gender', 'date_of_birth')
    list_filter = ('gender', 'country')
    search_fields = ('full_name', 'email')

admin.site.register(Products)