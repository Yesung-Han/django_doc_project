import null as null
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import datetime

# Create your models here.
class Post(models.Model):
    title_text = models.CharField(max_length=50)
    writer = models.ForeignKey(User, null= True, on_delete=models.CASCADE)

    create_date = models.DateTimeField('Created date', auto_now_add= True)
    modify_date = models.DateTimeField('Modified date')
    content = models.TextField("CONTENT")

    parent_post = models.ForeignKey('self', null= True, blank= True, on_delete=models.CASCADE)
    g_order = models.IntegerField(default=0, blank= True)
    depth = models.IntegerField(default=0, blank= True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title_text

    def get_absolute_url(self):
        return reverse("myapp:post_detail",args=(self.id,))

    def get_comment_count(self):
        comments = Comment.objects.filter(linkedPost_id=self.id)
        return len(comments)

    def initRePost(self, parentPost):
        self.parent_post = parentPost
        self.g_order = parentPost.g_order
        self.depth = 1
        return


class Comment(models.Model):
    linkedPost = models.ForeignKey(Post, on_delete=models.CASCADE)

    create_date = models.DateTimeField('Created date', auto_now_add=True)
    modify_date = models.DateTimeField('Modified date')

    content = models.CharField(max_length=200)
    writer = models.ForeignKey(User, null= True, on_delete=models.CASCADE)

    parent_comment = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)

    def initReComment(self, parentComment):
        self.parent_comment = parentComment.id
        self.depth = 1
        return

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ('-modify_date',)

