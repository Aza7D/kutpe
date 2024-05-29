from django.contrib import admin

from .models import MentorTypeUser, ContactWithMentor


@admin.register(MentorTypeUser)
class MentorTypeUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'subjects', 'description')
    search_fields = ('user__full_name', 'user__email', 'user__username')


admin.site.register(ContactWithMentor)
