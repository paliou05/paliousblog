from django import forms
from models import Post


class AuthorForm(forms.Form):
    author = forms.CharField()
    title = forms.CharField()
    text = forms.CharField()
    created_date = forms.DateTimeField()
    published_date = forms.DateTimeField()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


