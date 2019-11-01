from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Idea(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, null=True, blank=True)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

class Comment_Idea(models.Model):
	idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='comments_idea')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	created = models.DateTimeField(default=timezone.now)
	Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies_idea')

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.body
