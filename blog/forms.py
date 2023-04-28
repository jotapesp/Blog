from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

class PostBlog(forms.ModelForm):
    title = forms.CharField(required=True, help_text="Enter post title")
    content = forms.CharField(required=True,
                            widget=forms.widgets.Textarea(
                            attrs={
                                "placeholder": "Type something."
                                }
                            ),
                            label ="",)

    class Meta:
        model = Post
        exclude = ('author',)

class PostComment(forms.ModelForm):
    content = forms.CharField(required=True,
                            widget=forms.widgets.Textarea(
                            attrs={
                                "placeholder": "Enter your comment"
                                }
                            ),
                            label ="Description",
                            help_text="Enter your comment here")

    class Meta:
        model = Comment
        exclude = ('author', 'post',)
