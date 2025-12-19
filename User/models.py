from django.db import models
from Guest.models import *
from JobProvider.models import *
# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=50,null=True)
    complaint_status=models.IntegerField(default=0)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_request(models.Model):
    request_date=models.DateField(auto_now_add=True)
    request_status=models.IntegerField(default=0)
    request_file=models.FileField(upload_to="Assets/RequestDocs/")
    job_id=models.ForeignKey(tbl_job,on_delete=models.CASCADE)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_examinationbody(models.Model):
    examination = models.ForeignKey(tbl_examination, on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    total_marks = models.IntegerField(default=0)
    examinationbody_status = models.IntegerField(default=0)

class tbl_examinationanswers(models.Model):
    examinationbody = models.ForeignKey(tbl_examinationbody, on_delete=models.CASCADE)
    question = models.ForeignKey(tbl_questions, on_delete=models.CASCADE)
    myanswer = models.ForeignKey(tbl_options, on_delete=models.CASCADE, related_name="myanswer", null=True)
    correct_answer = models.ForeignKey(tbl_options, on_delete=models.CASCADE,related_name="correct_answer")
    examinationanswers_statusq = models.IntegerField(default=0)

class tbl_timmer(models.Model):
    timmer = models.TimeField()
    exam = models.ForeignKey(tbl_examination, on_delete=models.CASCADE)
    timmer_status = models.IntegerField(default=0)

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=50)
    user =models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    jobprovider =models.ForeignKey(tbl_jobprovider,on_delete=models.CASCADE,null=True)
