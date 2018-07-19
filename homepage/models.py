from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    names = models.IntegerField(default=0, null=True, blank=True)
    ordinances = models.IntegerField(default=0, null=True, blank=True)
    raffle = models.TextField(default='A')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
