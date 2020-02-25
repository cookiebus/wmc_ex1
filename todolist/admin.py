from django.contrib import admin
from todolist.models import Todo, Activity, Question
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','updated_at')
class ActivityAdmin(admin.ModelAdmin):
    list_displace = ('id','theme', 'start','end')
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Todo, TodoAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Question, QuestionAdmin)
