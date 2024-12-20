from django.contrib import admin
from .models import Platform, Duty, Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('owner', 'platform', 'created_at', 'due_date')
    list_filter = ('platform', 'created_at', 'due_date')
    search_fields = ('owner__username',)
# Register your models here.

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    search_fields = ('name', 'owner__username')

@admin.register(Duty)
class DutyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
