#-*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class Admin_Question(admin.ModelAdmin):

    #발행일 이 내용 보다 앞에 오게 함.
    #fields = ['pub_date', 'question_text']

    #목록 나누기
    fieldsets = [
        (None, {'fields' : ['question_text']}),
        ('Date Info', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, Admin_Question)
admin.site.register(Choice)

