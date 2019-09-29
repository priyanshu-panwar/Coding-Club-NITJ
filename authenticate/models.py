from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
	user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
	branch = models.ForeignKey('Branch', null=True, blank=True, on_delete=models.CASCADE)
	description = models.TextField(null=True, blank=True)
	contact = models.CharField(max_length=13, null=True, blank=True)
	preferred_language = models.ForeignKey('Languages', null=True, blank=True, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='profile_pics', null=True, blank=True)

	def __str__(self):
		return self.user.username


class Branch(models.Model):
	name = models.CharField(max_length=4)

	def __str__(self):
		return self.name


class Languages(models.Model):
	name = models.CharField(max_length=10)

	def __str__(self):
		return self.name


def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
