from django.db import models
from Guest.models import *
from Admin.models import *
# Create your models here.
class tbl_job(models.Model):
    job_title=models.CharField(max_length=50)
    job_content=models.CharField(max_length=50)
    job_requriedage=models.CharField(max_length=50)
    job_experience=models.CharField(max_length=50)
    job_salary=models.CharField(max_length=50)
    job_lastdate=models.DateField()
    job_date=models.DateField(auto_now_add=True)
    job_status=models.IntegerField(default=0)
    jobprovider_id=models.ForeignKey(tbl_jobprovider,on_delete=models.CASCADE)
    jobcategory_id=models.ForeignKey(tbl_jobcategory,on_delete=models.CASCADE)
    jobtype_id=models.ForeignKey(tbl_jobtype,on_delete=models.CASCADE)

class tbl_jobqualification(models.Model):
    qualification_id=models.ForeignKey(tbl_qualification,on_delete=models.CASCADE)
    job_id=models.ForeignKey(tbl_job,on_delete=models.CASCADE)

class tbl_examination(models.Model):
    examination_name=models.CharField(max_length=50) 
    examination_mark=models.CharField(max_length=50) 
    # examination_qno=models.CharField(max_length=50)
    examination_time=models.CharField(max_length=50) 
    examination_status = models.IntegerField(default=0)
    time = models.TimeField(null=True)
    start_time = models.TimeField(null=True)
    job=models.ForeignKey(tbl_job,on_delete=models.CASCADE,null=True)

class tbl_questions(models.Model):
    question=models.CharField(max_length=100) 
    examination=models.ForeignKey(tbl_examination,on_delete=models.CASCADE)

class tbl_options(models.Model):
    questions=models.ForeignKey(tbl_questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    status = models.BooleanField() 