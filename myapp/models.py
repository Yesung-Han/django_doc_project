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
    modify_date = models.DateTimeField('Modified date', auto_now = True)
    content = models.TextField("CONTENT")

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title_text

    def get_absolute_url(self):
        return reverse("myapp:post_detail",args=(self.id,))

class Comment(models.Model):
    linkedPost = models.ForeignKey(Post, on_delete=models.CASCADE)

    create_date = models.DateTimeField('Created date', auto_now_add=True)
    modify_date = models.DateTimeField('Modified date', auto_now=True)

    content = models.CharField(max_length=200)
    writer = models.ForeignKey(User, null= True, on_delete=models.CASCADE)



