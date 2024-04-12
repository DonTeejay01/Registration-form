from django.db import models

class gradregistrationModel(models.Model):
    infoID = models.AutoField(primary_key = True)
    lastname = models.CharField(max_length=60)
    firstname = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=60)
    department = models.CharField(max_length=100)
    matricNum = models.CharField(max_length=30)
    parentLastname = models.CharField(max_length=60)
    parentFirstname = models.CharField(max_length=60)
    parentEmail = models.EmailField()
    parentPhone= models.CharField(max_length=60)


    class Meta:
        db_table="registrationInfo_tbl"




# Create your models here.
