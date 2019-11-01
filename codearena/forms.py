from django import forms
from .models import Solution

class SolutionForm(forms.ModelForm):
	class Meta:
		model = Solution
		fields = ('code',)

	code = forms.CharField(label="", max_length=2000, 
		widget=forms.Textarea(
			attrs={
			'class':'form-control', 
			'placeholder':'Code',
			}))
