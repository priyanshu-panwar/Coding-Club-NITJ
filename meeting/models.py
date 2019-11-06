from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
    topic = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return self.topic
