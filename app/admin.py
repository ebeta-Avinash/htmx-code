from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

