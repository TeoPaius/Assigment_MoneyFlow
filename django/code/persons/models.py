from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.TextField()


class Friendship(models.Model):
    personA = models.ForeignKey(Person, on_delete = models.CASCADE, related_name="personA")
    personB = models.ForeignKey(Person, on_delete = models.CASCADE, related_name="personB")