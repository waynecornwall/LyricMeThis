from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Song(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    lyrics = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        word_count = len(self.lyrics)
        word_max = 50
        if word_count > word_max:
            output = f'{self.lyrics} ...'
        else:
            output = self.lyrics
        return output

