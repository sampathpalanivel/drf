from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
