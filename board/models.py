from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=64)
    alias = models.CharField(max_length=64)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " (" + self.alias + ')'

class Timeslot(models.Model):
    person = models.ForeignKey(Person)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField(null=True)
