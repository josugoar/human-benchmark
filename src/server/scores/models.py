from django.db import models


class Score(models.Model):
    accuracy = models.FloatField(name='accuracy')
    wpm = models.IntegerField(name='words_per_minute')
    cpm = models.IntegerField(name='characters_per_minute')
    time = models.FloatField(name='time')

    def __str__(self):
        return self.accuracy
