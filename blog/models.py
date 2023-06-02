from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=60,required=True)
    branch = models.CharField(max_length=20,required=True)
    start_year = models.IntegerField(required=True)
    end_year = models.IntegerField(required=True)

    def __str__(self):
        return  self.name
    
class School(models.Model):
    standard = models.IntegerField(required=True)
    school_name = models.CharField(required=True)
    start_year = models.IntegerField(required=True)
    end_year = models.IntegerField(required=True)
    percentage = models.DecimalField(requied=True)

    def __str__(self):
        return  self.standard

class Certifications(models.Model):
    c_name = models.CharField(max_length=50,required=True)
    provider = models.CharField(max_length=30,required=True)
    c_id = models.CharField(max_length=40)
    c_link = models.URLField(max_length=200)





