from django.shortcuts import render
from .models import Contact
from .forms import ContactForm, SubscriptionForm
from newsletter.models import NewsletterUsers

def home(request):
	form = ContactForm()
	u_form = SubscriptionForm()
	context = {
		'form': form,
		'u_form': u_form,
	}
	
	return render(request, 'core/index.html', context)

def subscription(request):
	if request.method == 'POST':
		form = SubscriptionForm(request.POST)
		if form.is_valid():
			sub = NewsletterUsers()
			sub.email = form.cleaned_data['email']
			sub.save()
			context = {'form': SubscriptionForm()}
			return render(request, 'core/thanks.html', context)
	else:
		form = SubscriptionForm()
	return render(request, 'core/index.html', {'form': form })

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			con = Contact()
			con.name = form.cleaned_data['name']
			con.email = form.cleaned_data['email']
			con.subject = form.cleaned_data['subject']
			con.message = form.cleaned_data['message']
			con.save()
			context = {'form': ContactForm()}
			return render(request, 'core/thanks2.html', context)
	else:
		form = ContactForm()

	return render(request, 'core/index.html', {'form': form})

