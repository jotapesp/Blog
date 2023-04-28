from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime

class Post(models.Model):
    title = models.CharField(max_length=255, help_text="Enter post title", null=True, blank=True)
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-date', 'title']
        permissions = (("can_post", "Write a post"),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=400, help_text="Enter your comment here. Max 400 char.")
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['date', 'post']
        permissions = (('can_delete_comment', 'Delete comment'),)

    def __str__(self):
        return f'{self.id} - {self.author.username} on {self.date}'

class Blogger(models.Model):
    name = models.CharField(max_length=255, help_text="Enter full name.")
    birth = models.DateField('Birth date', null=True, blank=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField('Biography', max_length=1000)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])
