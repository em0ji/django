from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone", "email", 'create_at']
    list_display_links = ("name",)
    list_filter = ('create_at', 'name')
    search_fields = ('name', 'email', "phone")
    