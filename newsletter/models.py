from django.db import models
from django.utils import timezone

class NewsletterUsers(models.Model):
	email = models.EmailField()
	date_added = models.DateTimeField(default=timezone.now, blank=True, null=True)

	def __str__(self):
		return self.email

