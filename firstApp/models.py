
# Create your models here.
from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=60)
    branch = models.CharField(max_length=20)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return  self.name
    
class School(models.Model):
    standard = models.IntegerField()
    school_name = models.CharField(max_length=30)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    percentage = models.DecimalField(max_digits=2,decimal_places=2)

    def __str__(self):
        return  self.standard

class Certifications(models.Model):
    c_name = models.CharField(max_length=50)
    provider = models.CharField(max_length=30)
    c_id = models.CharField(max_length=40)
    c_link = models.URLField(max_length=200)





