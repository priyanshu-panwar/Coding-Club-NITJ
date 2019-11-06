from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	subject = models.CharField(max_length=30, null=True, blank=True)
	message = models.CharField(max_length=1000)

	def __str__(self):
		return self.name

class TeamMember(models.Model):
	name = models.CharField(max_length=30)
	post = models.CharField(max_length=30)
	profile_pic = models.ImageField(upload_to='profile_pic', null=True, blank=True)
	facebook = models.URLField(null=True, blank=True)
	linkedin = models.URLField(null=True, blank=True)
	github = models.URLField(null=True, blank=True)
	
	def __str__(self):
		return self.name

class Event(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='events')

	def __str__(self):
		return self.name