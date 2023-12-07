from django.db import models


class Challenger(models.Model):
    user_id = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64, unique=True)
    honor = models.IntegerField(default=0)
    totalCompleted = models.IntegerField(default=0)
    name = models.CharField(max_length=64)


class CodewarsGroup(models.Model):
    name = models.CharField(max_length=128, unique=True)
    challengers = models.ManyToManyField(Challenger)


class Chellange(models.Model):
    chellanger = models.ForeignKey(Challenger, on_delete=models.CASCADE, related_name='chellanges')
    chellange_id = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    completedAt = models.DateTimeField()
    slug = models.SlugField()
