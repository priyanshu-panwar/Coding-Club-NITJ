from django import forms
from .models import Comment_Idea, Idea
from pagedown.widgets import PagedownWidget


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment_Idea
		fields = ('body',)

	body = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Comment'}))
    

class PostForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget=PagedownWidget())
    class Meta:
        model = Idea
        fields = ('title', 'content',)