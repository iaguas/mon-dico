from django.contrib.auth.models import User
from django.db import models


class Word(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    word = models.CharField(max_length=30, verbose_name="mot")
    sentence = models.CharField(max_length=150, verbose_name="phrase")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word
