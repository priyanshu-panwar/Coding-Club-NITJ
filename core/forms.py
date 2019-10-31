from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(
		max_length=30,
		label="",
		widget=forms.TextInput(
				attrs={
					'name': 'name',
					'placeholder': 'Full Name',
					'class': 'form-control'
				}
			)
		)

	email = forms.EmailField(
		max_length=254,
		label="",
		widget=forms.EmailInput(
				attrs={
					'name': 'email',
					'placeholder': 'Email Address',
					'class': 'form-control'

				}
			)
		)

	subject = forms.CharField(
		max_length=100,
		label="",
		widget=forms.TextInput(
				attrs={
					'name': 'subject',
					'placeholder': 'Subject',
					'class': 'form-control'
				}
			)
		)

	message = forms.CharField(
		max_length=1000,
		label="",
		widget=forms.Textarea(
				attrs={
					'name': 'message',
					'placeholder': 'Message',
					'class': 'form-control'
				}
			)
		)


class SubscriptionForm(forms.Form):
	email = forms.EmailField(
		max_length=254,
		label="",
		widget=forms.EmailInput(
				attrs={
					'name': 'email',
					'placeholder': 'Email Address',
					'class': 'form-control'

				}
			)
		)
