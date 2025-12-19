from django.shortcuts import render
from Admin.models import *
from Guest.models import *
from User.models import *
# Create your views here.
def District(request):
    districtDatas = tbl_district.objects.all()
    if request.method=="POST":
        districtname=request.POST.get('txt_districtname')
        checkdistrict=tbl_district.objects.filter(district_name=districtname).count()
        if checkdistrict > 0:
            return render(request,"Admin/District.html",{'msg':"District Already Exited"})
        else:
            tbl_district.objects.create(district_name=districtname)
            return render(request,'Admin/District.html',{'msg':'Inserted Successfully'})
    else:
        return render(request,'Admin/District.html',{'districtDatas':districtDatas})

def DeleteDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,'Admin/District.html',{'msg':'Deleted Successfully'})

def EditDistrict(request,eid):
    districtOne=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        checkdistrict=tbl_district.objects.filter(district_name=request.POST.get("txt_districtname")).count()
        if checkdistrict > 0:
            return render(request,"Admin/District.html",{'msg':"District Already Exited"})
        else:
            districtOne.district_name=request.POST.get("txt_districtname")
            districtOne.save()
            return render(request,'Admin/District.html',{'msg':'Edited Successfully'})
    else:
        return render(request,"Admin/District.html",{"districtOne":districtOne})
def Category(request):
    categoryDatas = tbl_category.objects.all()
    if request.method=="POST":
        categoryname=request.POST.get('txt_categoryname')
        tbl_category.objects.create(category_name=categoryname)
        return render(request,'Admin/Category.html',{'msg':'Inserted Successfully'})
    else:
        return render(request,'Admin/Category.html',{'categoryDatas':categoryDatas})
def DeleteCategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return render(request,'Admin/Category.html',{'msg':'Delete Successfully'})

def EditCategory(request,eid):
    categoryOne=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        
        categoryOne.category_name=request.POST.get("txt_categoryname")
        categoryOne.save()
        return render(request,'Admin/Category.html',{'msg':'Edited Successfully'})
    else:
        return render(request,'Admin/Category.html',{"categoryOne":categoryOne})
def Place(request):
    districtDatas = tbl_district.objects.all()
    placeDatas = tbl_place.objects.all()
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        placename=request.POST.get('txt_placename')
        tbl_place.objects.create(place_name=placename,district=district)
        return render(request,'Admin/Place.html',{'msg':'Inserted Successfully'})
    else:
        return render(request,'Admin/Place.html',{'districtDatas':districtDatas ,'placeDatas':placeDatas})
def DeletePlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return render(request,'Admin/Place.html',{'msg':'Deleted Successfully'})

def EditPlace(request,eid):
    districtDatas = tbl_district.objects.all()
    placeOne=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        placeOne.place_name=request.POST.get("txt_placename")
        placeOne.district = district
        placeOne.save()
        return render(request,'Admin/Place.html',{'msg':'Edited Successfully'})
    else:
        return render(request,"Admin/Place.html",{"placeOne":placeOne,'districtDatas':districtDatas})

def Subcategory(request):
    categoryDatas = tbl_category.objects.all()
    subcategoryDatas = tbl_subcategory.objects.all()
    if request.method=="POST":
        category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        subcategoryname=request.POST.get('txt_subcategory')
        tbl_subcategory.objects.create(subcategory_name=subcategoryname,category=category)
        return render(request,'Admin/Subcategory.html',{'msg':'Inserted Successfully'})
    else:
        return render(request,'Admin/Subcategory.html',{'categoryDatas':categoryDatas ,'subcategoryDatas':subcategoryDatas})
def DeleteSubcategory(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return render(request,'Admin/Subcategory.html',{'msg':'Deleted Successfully'})

def EditSubcategory(request,eid):
    categoryDatas = tbl_category.objects.all()
    subcategoryOne=tbl_subcategory.objects.get(id=eid)
    if request.method=="POST":
        category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        subcategoryOne.subcategory_name=request.POST.get("txt_subcategory")
        subcategoryOne.category = category
        subcategoryOne.save()
        return render(request,'Admin/Subcategory.html',{'msg':'Edited Successfully'})
    else:
        return render(request,"Admin/Subcategory.html",{"subcategoryOne":subcategoryOne,'categoryDatas':categoryDatas})

def AdminRegistration(request):
    adminDatas = tbl_admin.objects.all()
    if request.method=="POST":
        name = request.POST.get("txt_name")
        email = request.POST.get("txt_email")
        password = request.POST.get("txt_password")
        checkemail=tbl_admin.objects.filter(admin_email=email).count()
        if checkemail > 0:
            return render(request,"Admin/AdminRegistration.html",{'msg':"Email Already Exited"})
        else:
            tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)
            return render(request,'Admin/AdminRegistration.html',{'msg':'Inserted Successfully'})
    else:
        return render(request,'Admin/AdminRegistration.html',{"adminDatas":adminDatas})

def DeleteAdmin(request,did):
    tbl_admin.objects.get(id=did).delete()
    return render(request,'Admin/AdminRegistration.html',{'msg':'Deleted Successfully'})

def UserList(request):
    userdata = tbl_user.objects.all()
    
    return render(request,'Admin/UserList.html',{"userdata":userdata})

def ViewComplaint(request):
    complaintdata = tbl_complaint.objects.filter(complaint_status=0)
    complaintone = tbl_complaint.objects.filter(complaint_status=1)
    return render(request,'Admin/ViewComplaint.html',{"complaintdata":complaintdata,"complaintone":complaintone})

def Reply(request,eid):
    complaintone=tbl_complaint.objects.get(id=eid)
    if request.method == "POST":
        complaintone.complaint_reply=request.POST.get("txt_reply")
        complaintone.complaint_status=1
        complaintone.save()
        return render(request,'Admin/Reply.html',{'msg':'Replied Successfully...'})
    else:
        return render(request,'Admin/Reply.html',{"complaintone":complaintone})

def JobType(request):
    jobtypedata=tbl_jobtype.objects.all()
    if request.method == "POST":
        jobtype = request.POST.get("txt_type")
        checkjobtype=tbl_jobtype.objects.filter(jobtype_name=jobtype).count()
        if checkjobtype > 0:
            return render(request,"Admin/JobType.html",{'msg':"JobType Already Exited"})
        else:
            tbl_jobtype.objects.create(jobtype_name=jobtype)
            return render(request,'Admin/JobType.html',{'msg':'Inserted Successfully..'})
    else:
        return render(request,'Admin/JobType.html',{"jobtypedata":jobtypedata})

def DeleteJobType(request,did):
    tbl_jobtype.objects.get(id=did).delete()
    return render(request,'Admin/JobType.html',{'msg':'Deleted Successfully'})

def JobCategory(request):
    jobcategorydata=tbl_jobcategory.objects.all()
    if request.method == "POST":
        jobcategory = request.POST.get("txt_jobcategory")
        checkjobcategory=tbl_jobcategory.objects.filter(jobcategory_name=jobcategory).count()
        if checkjobcategory > 0:
            return render(request,"Admin/JobCategory.html",{'msg':"JobCategory Already Exited"})
        else:
            tbl_jobcategory.objects.create(jobcategory_name=jobcategory)
            return render(request,'Admin/JobCategory.html',{'msg':'Inserted Successfully..'})
    else:
        return render(request,'Admin/JobCategory.html',{"jobcategorydata":jobcategorydata})

def DeleteJobCategory(request,did):
    tbl_jobcategory.objects.get(id=did).delete()
    return render(request,'Admin/JobCategory.html',{'msg':'Deleted Successfully'})

def Qualification(request):
    qualificationdata=tbl_qualification.objects.all()
    if request.method == "POST":
        qualification = request.POST.get("txt_qualification")
        tbl_qualification.objects.create(qualification_name=qualification)
        return render(request,'Admin/Qualification.html',{'msg':'Inserted Successfully..'})
    else:
        return render(request,'Admin/Qualification.html',{"qualificationdata":qualificationdata})

def DeleteQualification(request,did):
    tbl_qualification.objects.get(id=did).delete()
    return render(request,'Admin/Qualification.html',{'msg':'Deleted Successfully'})

def JobproviderVerification(request):
    pending = tbl_jobprovider.objects.filter(jobprovider_status=0)
    accept = tbl_jobprovider.objects.filter(jobprovider_status=1)
    reject = tbl_jobprovider.objects.filter(jobprovider_status=2)
    return render(request,'Admin/JobproviderVerification.html',{"pending":pending,"accept":accept,"reject":reject})

def Accept(request,aid):
    jobproviderdata = tbl_jobprovider.objects.get(id=aid)
    jobproviderdata.jobprovider_status=1
    jobproviderdata.save()
    return render(request,"Admin/JobproviderVerification.html",{'msg':"Request Accepted.."})

def Reject(request,rid):
    jobproviderdata = tbl_jobprovider.objects.get(id=rid)
    jobproviderdata.jobprovider_status=2
    jobproviderdata.save()
    return render(request,"Admin/JobproviderVerification.html",{'msg':"Request Rejected.."})

def Feedback(request):
    user=tbl_user.objects.all()
    userfeedback=tbl_feedback.objects.filter(user__in=user)
    jobprovider=tbl_jobprovider.objects.all()
    jobproviderfeedback=tbl_feedback.objects.filter(jobprovider__in=jobprovider)
    return render(request,"Admin/Feedback.html",{'userfeedback':userfeedback,'jobproviderfeedback':jobproviderfeedback})

def HomePage(request):
    admindata = tbl_admin.objects.get(id=request.session['aid'])
    return render(request,"Admin/HomePage.html",{'admindata':admindata})