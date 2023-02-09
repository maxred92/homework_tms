from .models import Comment, Games
from django import forms


class CommentForm(forms.ModelForm):  
    class Meta:  
        model = Comment  
        fields = ('name', 'email', 'body', 'rating')
        widgets = {
            'body':  forms.Textarea(attrs={'cols': 30, 'rows': 8}),
        }

