from django.contrib import admin
from .models import Questions, Answers, ByUser

# Register your models here.

# admin.site.register(Queries)

@admin.register(Questions)

class QuestAdmin(admin.ModelAdmin):
    list_display = [
        'title'
    ]


class AnswerInLineModel(admin.TabularInline):
    model = Answers  
    fields = [
        'answer_text',
        'likes',
        'dislikes'
    ]

class QuestionsAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'date_created'
    ]
    list_display = [
        'title'
    ]
    inlines = [
        AnswerInLineModel
    ]

@admin.register(Answers)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'questions',
        'byUser'
    ]

@admin.register(ByUser)
class ByUserAdmin(admin.ModelAdmin):
    fields = [
        'username',
        'rating'
    ]

