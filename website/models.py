from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=10)
    college = models.CharField(max_length=200)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name