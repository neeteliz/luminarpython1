from django.db import models

# Create your models here.
class Emp(models.Model):
    eid=models.IntegerField(unique="True")
    ename=models.CharField(max_length=250)
    def __str__(self):
        return self.ename+str(self.eid)


class Empdetail(models.Model):
    esal=models.IntegerField()
    design=models.CharField(max_length=250)
    eid=models.ForeignKey(Emp,on_delete=models.CASCADE)

    def __str__(self):
        return self.design+self.esal+self.eid