from django import forms
from home.models import Post, Comment


class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write something here...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your comment...'
        }
    ))

    class Meta:
        model = Comment
        fields = ('comment',)
