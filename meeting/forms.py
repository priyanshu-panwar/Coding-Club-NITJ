from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('topic', 'question_text', )

	topic = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Topic'}))
	question_text = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Question'}))
