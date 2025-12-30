from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from JobProvider.models import *
from django.http import HttpResponse
from django.http import JsonResponse
import json
from datetime import time, datetime, timedelta,date


# Create your views here.
def HomePage(request):
    userdata = tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/HomePage.html',{'user':userdata})

def MyProfile(request):
    userdata = tbl_user.objects.get(id=request.session['uid']) 
    return render(request,'User/MyProfile.html',{'user':userdata})

def EditProfile(request):
    userdata = tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        checkuser=tbl_user.objects.filter(user_email=email).count()
        if checkuser > 0:
            return render(request,"User/EditProfile.html",{'msg':"Email Already Exited"})
        else:
            userdata.user_name = name
            userdata.user_email = email
            userdata.user_contact = contact
            userdata.user_address = address
            userdata.save()
            return render(request,'User/EditProfile.html',{"msg":"Profile Updated.."})
    else:
        return render(request,'User/EditProfile.html',{'user':userdata})

def ChangePassword(request):
    userdata = tbl_user.objects.get(id=request.session['uid'])
    userpass= userdata.user_password
    if request.method == "POST":
        oldpassword=request.POST.get("txt_oldpassword")
        newpassword=request.POST.get("txt_newpassword")
        repassword=request.POST.get("txt_repassword")
        if userpass == oldpassword:
            if newpassword == repassword:
                userdata.user_password = newpassword
                userdata.save()
                return render(request,'User/ChangePassword.html',{"msg":"Password Changed.."})
            else:
                return render(request,'User/ChangePassword.html',{"msg":"Password Mismatch.."})
        else:
            return render(request,'User/ChangePassword.html',{"msg":"Password Incorrect.."})
    else:
        return render(request,'User/ChangePassword.html',{'user':userdata})

def Complaint(request):
    complaintdata= tbl_complaint.objects.filter(user_id=request.session['uid'])
    if request.method == "POST":
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        user= tbl_user.objects.get(id=request.session['uid'])
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user_id=user)
        return render(request,'User/Complaint.html',{'msg':'Complaint Registered...'})
    else:
        return render(request,'User/Complaint.html',{'complaintdata':complaintdata})

def DeleteComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return render(request,'User/Complaint.html',{'msg':'Deleted Successfully..'})

def ViewJob(request):
    jobdata=tbl_job.objects.filter(job_lastdate__gte=date.today())
    print(jobdata)

    return render(request,'User/ViewJob.html',{'jobdata':jobdata})

def Request(request,id):
    if request.method == "POST":
        file=request.FILES.get("file_photo")
        job=tbl_job.objects.get(id=id)
        user= tbl_user.objects.get(id=request.session['uid'])
        tbl_request.objects.create(request_file=file,job_id=job,user_id=user)
        return render(request,'User/Request.html',{'msg':'File Inserted..'})
    else:
        return render(request,'User/Request.html')
    
def MyRequest(request):
    reqdata = tbl_request.objects.filter(user_id=request.session['uid'])
    return render(request,"User/MyRequest.html",{"reqdata":reqdata})

def viewexam(request,id):
    exam = tbl_examination.objects.filter(job=id)

    for i in exam:
        questioncount = tbl_questions.objects.filter(examination=i.id).count()
        i.qtcount = questioncount
        exambodycount = tbl_examinationbody.objects.filter(examination=i.id,user=request.session["uid"],examinationbody_status=1).count()
        if exambodycount > 0:
            i.examstatus = 1
            
    return render(request,"User/ViewExam.html",{'exam':exam})

def viewquestion(request,id):
    question = tbl_questions.objects.filter(examination=id)
    optioncount = 0
    for i in question:
        count = tbl_options.objects.filter(questions=i.id).count()
        if count > 0:
            optioncount = optioncount + 1
    examcount = tbl_examinationbody.objects.filter(examination=id,user=request.session["uid"]).count()
    if examcount > 0:
        exambodyid = tbl_examinationbody.objects.get(examination=id,user=request.session["uid"])
        return render(request,"User/ViewQuestion.html",{'questions':question,"exambodyid":exambodyid.id,"optioncount":optioncount,"examination_id":id})
    else:
        exambodyid = tbl_examinationbody.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),examination=tbl_examination.objects.get(id=id))
        return render(request,"User/ViewQuestion.html",{'questions':question,"exambodyid":exambodyid.id,"optioncount":optioncount,"examination_id":id})

def ajaxexamanswer(request):
    exam_answer = request.GET.get('answers')
    answers_dict = json.loads(exam_answer)
    for question_key, option_id in answers_dict.items():
        questionid = question_key.split("_")[1]
        options = tbl_options.objects.get(questions=questionid,status=True)
        if option_id == None:
            tbl_examinationanswers.objects.create(examinationbody=tbl_examinationbody.objects.get(id=request.GET.get('exambodyid')),question=tbl_questions.objects.get(id=questionid),correct_answer=tbl_options.objects.get(id=options.id))
        else:
            tbl_examinationanswers.objects.create(examinationbody=tbl_examinationbody.objects.get(id=request.GET.get('exambodyid')),question=tbl_questions.objects.get(id=questionid),myanswer=tbl_options.objects.get(id=option_id),correct_answer=tbl_options.objects.get(id=options.id))
    exambody = tbl_examinationbody.objects.get(id=request.GET.get('exambodyid'))
    exambody.examinationbody_status = 1
    exambody.save()
    return JsonResponse({"msg":"Examination Submitted Sucessfully..."})

def ajaxtimer(request):
    exam = tbl_examination.objects.get(id=request.GET.get('exam'))
    timecount = tbl_timmer.objects.filter(exam=exam).count()
    if timecount > 0:
        timer_obj = tbl_timmer.objects.get(exam=exam)
        if timer_obj.timmer > time(0, 0, 0):
            current_datetime = datetime.combine(datetime.today(), timer_obj.timmer)
            new_datetime = current_datetime - timedelta(seconds=1)
            new_time = new_datetime.time()
            timer_obj.timmer = new_time
            timer_obj.save()
            time_str = new_time.strftime("%H:%M:%S")
            return JsonResponse({"msg": time_str,"status":False})
        else:
            exam.examination_status = 2
            exam.save()
            return JsonResponse({"msg": "Time's up","status":True})
    else:
        tbl_timmer.objects.create(exam=exam,timmer=exam.time)
        return JsonResponse({"msg": ""})

def successer(request):
    return render(request,"User/Success.html")

def Feedback(request):
    if request.method == "POST":
        feedback=request.POST.get("txt_feedback")
        user=tbl_user.objects.get(id=request.session['uid'])
        tbl_feedback.objects.create(feedback_content=feedback,user=user)
        return render(request,"User/Feedback.html",{'msg':'Feedback Submitted'})
    else:
        return render(request,"User/Feedback.html")
    
def Logout(request):
    del request.session['uid']
    return redirect('Guest:Login')