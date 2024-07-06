from django.forms import ModelForm
from django import forms
from content.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'likes', 'dislikes']
        exclude = ["id"]