from django.contrib import admin

# Register your models here.
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3


class Post_Admin(admin.ModelAdmin):


    inlines = [CommentInline]

    list_display = ('title_text','writer','modify_date')


admin.site.register(Post, Post_Admin)