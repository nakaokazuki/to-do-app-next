from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "scheduled_at", "location", "is_completed", "updated_at")
    list_filter = ("is_completed",)
    search_fields = ("title", "location", "detail")