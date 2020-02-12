from django.db import models

# Create your models here.
class Employee(models.Model):
    ename= models.CharField(max_length=250)
    eid= models.CharField(max_length=8)
    esal= models.IntegerField()
    design = models.CharField(max_length=260)

    def __str__(self):
        return self.ename+self.eid+str(self.esal)+self.design

