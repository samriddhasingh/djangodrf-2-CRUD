from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=1000)
    roll=models.IntegerField()
    city=models.CharField(max_length=1000)

    