from django.db import models
from Admin.models import *
# Create your models here.

class tbl_user(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_contact = models.CharField(max_length=50)
    user_address = models.CharField(max_length=100)
    user_gender = models.CharField(max_length=50)
    user_dob = models.DateField()
    user_password = models.CharField(max_length=50)
    user_photo = models.FileField(upload_to="Assets/UserDocs/")
    place = models.ForeignKey(tbl_place,on_delete=models.CASCADE)

class tbl_jobprovider(models.Model):
   jobprovider_name = models.CharField(max_length=50)
   jobprovider_email = models.CharField(max_length=50)
   jobprovider_contact = models.CharField(max_length=50)
   jobprovider_address = models.CharField(max_length=100)
   jobprovider_photo = models.FileField(upload_to="Assets/JobProviderDocs/")
   jobprovider_proof = models.FileField(upload_to="Assets/JobProviderDocs/")
   jobprovider_status = models.IntegerField(default=0)
   jobprovider_doj = models.DateField(auto_now_add=True)
   jobprovider_password = models.CharField(max_length=50)
   place = models.ForeignKey(tbl_place,on_delete=models.CASCADE)
