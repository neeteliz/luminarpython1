from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=250)
    age= models.CharField(max_length=8)
    crse= models.CharField(max_length=260)

    def __str__(self):
        return self.name+str(self.age)+self.crse
