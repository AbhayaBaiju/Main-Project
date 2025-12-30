from django.shortcuts import render,redirect
from Guest.models import *
from JobProvider.models import *
from Admin.models import *
from User.models import *
from django.http import JsonResponse
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def HomePage(request):
    jobproviderdata = tbl_jobprovider.objects.get(id=request.session['jid'])
    return render(request,'JobProvider/HomePage.html',{'jobprovider':jobproviderdata})

def MyProfile(request):
    jobproviderdata = tbl_jobprovider.objects.get(id=request.session['jid']) 
    return render(request,'JobProvider/MyProfile.html',{'jobprovider':jobproviderdata})

def EditProfile(request):
    jobproviderdata = tbl_jobprovider.objects.get(id=request.session['jid'])
    if request.method == "POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        checkjobprovider=tbl_jobprovider.objects.filter(jobprovider_email=email).count()
        if checkjobprovider > 0:
            return render(request,"JobProvider/EditProfile.html",{'msg':"Email Already Exited"})
        else:
            jobproviderdata.jobprovider_name = name
            jobproviderdata.jobprovider_email = email
            jobproviderdata.jobprovider_contact = contact
            jobproviderdata.jobprovider_address = address
            jobproviderdata.save()
            return render(request,'JobProvider/EditProfile.html',{"msg":"Profile Updated.."})
    else:
        return render(request,'JobProvider/EditProfile.html',{'jobprovider':jobproviderdata})

def ChangePassword(request):
    jobproviderdata = tbl_jobprovider.objects.get(id=request.session['jid'])
    jobproviderpass= jobproviderdata.jobprovider_password
    if request.method == "POST":
        oldpassword=request.POST.get("txt_oldpassword")
        newpassword=request.POST.get("txt_newpassword")
        repassword=request.POST.get("txt_repassword")
        if jobproviderpass == oldpassword:
            if newpassword == repassword:
                jobproviderdata.jobprovider_password = newpassword
                jobproviderdata.save()
                return render(request,'JobProvider/ChangePassword.html',{"msg":"Password Changed.."})
            else:
                return render(request,'JobProvider/ChangePassword.html',{"msg":"Password Mismatch.."})
        else:
            return render(request,'JobProvider/ChangePassword.html',{"msg":"Password Incorrect.."})
    else:
        return render(request,'JobProvider/ChangePassword.html',{'jobprovider':jobproviderdata})
    
def Job(request):
    jobdata = tbl_job.objects.all()
    jobtypedata = tbl_jobtype.objects.all()
    jobcategorydata = tbl_jobcategory.objects.all()
    jobproviderId = tbl_jobprovider.objects.get(id=request.session['jid'])
    if request.method == "POST":
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        age=request.POST.get("txt_age")
        experience=request.POST.get("txt_experience")
        salary=request.POST.get("txt_salary")
        lastdate=request.POST.get("txt_date")
        jobtype = tbl_jobtype.objects.get(id=request.POST.get("sel_jobtype"))
        jobcategory = tbl_jobcategory.objects.get(id=request.POST.get("sel_category"))
        tbl_job.objects.create(job_title=title,job_content=content,job_requriedage=age,job_experience=experience,job_salary=salary,job_lastdate=lastdate,jobcategory_id=jobcategory,jobtype_id=jobtype,jobprovider_id=jobproviderId)
        return render(request,'JobProvider/Job.html',{'msg':'Job Added Successfully...'})
    else:
        return render(request,'JobProvider/Job.html',{'jobcategorydata':jobcategorydata,'jobtypedata':jobtypedata,'jobdata':jobdata})
    
def DeleteJob(request,did):
    tbl_job.objects.get(id=did).delete()
    return render(request,'JobProvider/Job.html',{'msg':'Deleted Successfully..'})

def JobQualification(request,jid):
    qualificationdata=tbl_qualification.objects.all()
    jobqualificationdata=tbl_jobqualification.objects.all()
    if request.method == "POST":
        qualification=tbl_qualification.objects.get(id=request.POST.get('sel_qualification'))
        job=tbl_job.objects.get(id=jid)
        tbl_jobqualification.objects.create(qualification_id=qualification,job_id=job)
        return render(request,'JobProvider/JobQualification.html',{'msg':'Qualification Added..'})
    else:
        return render(request,'JobProvider/JobQualification.html',{'qualificationdata':qualificationdata,'jobqualificationdata':jobqualificationdata})
    
def DeleteJobqualification(request,did):
    tbl_jobqualification.objects.get(id=did).delete()
    return render(request,'JobProvider/JobQualification.html',{'msg':'Deleted Successfully..'})

def ViewRequest(request):
    viewrequestdata=tbl_request.objects.filter(user_id=request.session['uid'])
    return render(request,"JobProvider/ViewRequest.html",{"viewrequestdata":viewrequestdata})

def Accept(request,aid):
    reqdata = tbl_request.objects.get(id=aid)
    reqdata.request_status=1
    reqdata.save()
    return render(request,"JobProvider/ViewRequest.html",{'msg':"Request Accepted.."})

def Reject(request,rid):
    reqdata = tbl_request.objects.get(id=rid)
    reqdata.request_status=2
    reqdata.save()
    return render(request,"JobProvider/ViewRequest.html",{'msg':"Request Rejected.."})

def examinationdetails(request, id):
    exm=tbl_examination.objects.filter(job=id,examination_status=0)
    if  request.method=="POST":
        name=request.POST.get("txt_name")
        qno=request.POST.get("txt_qno")
        # no=request.POST.get("txt_no")
        ftime = request.POST.get("txt_ftime")
        ttime = request.POST.get("txt_ttime")

        ftime_obj = datetime.strptime(ftime, "%H:%M")
        ttime_obj = datetime.strptime(ttime, "%H:%M")
        time_diff = ttime_obj - ftime_obj
        total_seconds = time_diff.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        
        time = str(hours) +" hours and "+ str(minutes) +" minutes"
        tbl_examination.objects.create(examination_name=name,examination_mark=qno,examination_time=time,job=tbl_job.objects.get(id=id),time=str(time_diff),start_time=ftime)

    return render(request,'JobProvider/Exam.html',{'result':exm})    

def addquestions(request,id):
    que=tbl_questions.objects.filter(examination=id)
    if  request.method=="POST":
        examination=tbl_examination.objects.get(id=id)
        questions=request.POST.get("txt_question")
        tbl_questions.objects.create(question=questions,examination=examination)
    return render(request,'JobProvider/Question.html',{'result':que,'id':id})

def addoptions(request, id):
    que = tbl_options.objects.filter(questions=id)
    if request.method == "POST":
        questions = tbl_questions.objects.get(id=id)
        ans = request.POST.get("txt_answer")
        status = request.POST.get("txt_radio") == "True"
        count = tbl_options.objects.filter(questions=questions, status=True).count()
        if status and count > 0:
            return render(request, 'JobProvider/Option.html', {
                'msg': "Corrected Answer is already added",
                'result': que,
                'id': id
            })
        else:
            tbl_options.objects.create(
                answer=ans,
                questions=questions,
                status=status
            )
            return redirect("JobProvider:addoptions", id=id)
    else:
        return render(request, 'JobProvider/Option.html', {'result': que, 'id': id})
    
def delopt(request,id,did): 
    tbl_options.objects.get(id=id).delete()
    return redirect("JobProvider:addoptions",did)

def MyExam(request):
    result=tbl_examination.objects.filter(job__jobprovider_id=request.session['jid'])
    return render(request,"JobProvider/MyExam.html",{"result":result})

def viewexaminer(request, id):
    user = tbl_examinationbody.objects.filter(examination=id).select_related('user')
    return render(request,"JobProvider/ViewExaminer.html",{"examiners":user})

def ViewResult(request,id, uid):
    question = tbl_questions.objects.filter(examination=id).count()
    result = tbl_examinationanswers.objects.filter(examinationbody__examination=id,examinationbody__user=uid,examinationbody__examinationbody_status=1)
    if result[0].examinationbody.total_marks == 0:
        total = 0
        for i in result:
            if i.myanswer and i.myanswer.id == i.correct_answer.id:
                total += 1
        exambody = tbl_examinationbody.objects.get(examination=id,user=request.session["uid"],examinationbody_status=1)
        exambody.total_marks = total
        exambody.save()
    return render(request, "JobProvider/ViewResult.html",{"result":result,"question":question})

def Feedback(request):
    if request.method == "POST":
        feedback=request.POST.get("txt_feedback")
        jobprovider=tbl_jobprovider.objects.get(id=request.session['jid'])
        tbl_feedback.objects.create(feedback_content=feedback,jobprovider=jobprovider)
        return render(request,"JobProvider/Feedback.html",{'msg':'Feedback Submitted'})
    else:
        return render(request,"JobProvider/Feedback.html")

def SendMail(request,uid):
    userdata=tbl_user.objects.get(id=uid)
    email=userdata.user_email
    send_mail(
                            'Respected Sir/Madam ',#subject
                            "\rYou are selected for the job vecancy through the conducted examination." 
                            "Attend the interview that held at Progressive Muvattupuzha on next monday."
                            "Take your CV and essential certificates for attending the interview."
                            "\r"
                            "\r"
                            "\rAll The Best For Your Interview."
                            "\r By"
                            "\r CARRER HIVE" ,#body
                            settings.EMAIL_HOST_USER,
                            [email],
                        )
    return render(request,"JobProvider/MyExam.html",{'msg':"Mail Send"})

def Logout(request):
    del request.session['jid']
    return redirect('Guest:Login')