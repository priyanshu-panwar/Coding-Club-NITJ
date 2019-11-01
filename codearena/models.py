from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save

class Coding_Profile(models.Model):
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	score = models.IntegerField(null=True, blank=True)
	events_participated = models.ManyToManyField('Event', null=True, blank=True)

	def __str__(self):
		return self.student.username

class Event(models.Model):
	title = models.CharField(max_length=100)
	date_posted = models.DateTimeField(default=timezone.now)
	date_valid = models.DateTimeField('validity date')

	def __str__(self):
		return self.title

class Question(models.Model):
	event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
	text = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.text

class Solution(models.Model):
	coder = models.ForeignKey(User, on_delete=models.CASCADE)
	code = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.coder.username


def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = Coding_Profile.objects.create(student=kwargs['instance'])

post_save.connect(create_profile, sender=User)
