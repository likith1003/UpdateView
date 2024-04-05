from django.db import models

# Create your models here.

class School(models.Model):
    sname = models.CharField(max_length=50, primary_key=True)
    principal = models.CharField(max_length=50)
    contact = models.CharField(max_length=14)

    def __str__(self):
        return self.sname
    

class Student(models.Model):
    sname = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    stdname = models.CharField(max_length=50)
    stdage = models.IntegerField()

    def __str__(self):
        return self.stdname
    

