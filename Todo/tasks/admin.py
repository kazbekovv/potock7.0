from django.contrib import admin
from tasks.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'created')
    search_fields = ('title',)

admin.site.register(Task, TaskAdmin)
