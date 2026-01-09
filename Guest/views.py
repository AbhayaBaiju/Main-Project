from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,"Guest/index.html")

def UserRegistration(request):
    districtDatas = tbl_district.objects.all()
    if request.method == "POST":
        photo = request.FILES.get("file_photo")
        name = request.POST.get("txt_name")
        email = request.POST.get("txt_email")
        contact = request.POST.get("txt_contact")
        address = request.POST.get("txt_address")
        gender = request.POST.get("btn_gender")
        dob = request.POST.get("txt_dob")
        place = tbl_place.objects.get(id=request.POST.get("sel_place"))
        password = request.POST.get("txt_password")
        repassword = request.POST.get("txt_repassword")
        checkuseremail=tbl_user.objects.filter(user_email=email).count()
        checkjobprovioderemail=tbl_jobprovider.objects.filter(jobprovider_email=email).count()
        if checkuseremail > 0:
            return render(request,"Guest/UserRegistration.html",{'msg':"Email Already Exited"})
        elif checkjobprovioderemail > 0:
            return render(request,"Guest/UserRegistration.html",{'msg':"Email Already Exited"})
        else:

            if password == repassword :
                tbl_user.objects.create(user_name=name,user_email=email,user_contact=contact,user_address=address,user_gender=gender,user_dob=dob,user_password=password,place=place,user_photo=photo)
                return render(request,"Guest/UserRegistration.html",{'msg':"Registration Successfull"})
            else:
                return render(request,"Guest/UserRegistration.html",{'msg':"Password Mismatch"})
    else:
        return render(request,'Guest/UserRegistration.html',{'districtDatas':districtDatas})
    


def AjaxPlace(request):
    districtId = request.GET.get("did")
    place = tbl_place.objects.filter(district=districtId)
    return render(request,"Guest/AjaxPlace.html",{'place':place})

def Login(request):
    if request.method == "POST":
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')

        usercount = tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount = tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        jobprovidercount = tbl_jobprovider.objects.filter(jobprovider_email=email,jobprovider_password=password).count()
        
        if usercount > 0:
            userdata = tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid'] = userdata.id
            return redirect("User:HomePage")
        elif admincount > 0:
            admindata = tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid'] = admindata.id
            return redirect("Admin:HomePage")
        elif jobprovidercount > 0:
            jobproviderdata = tbl_jobprovider.objects.get(jobprovider_email=email,jobprovider_password=password)
            if jobproviderdata.jobprovider_status == 0:
                return render(request,"Guest/Login.html",{'msg':"Registration Pending.."})
            elif jobproviderdata.jobprovider_status == 2:
                return render(request,"Guest/Login.html",{'msg':"Registration Rejected.."})
            else:
                request.session['jid'] = jobproviderdata.id
                return redirect("JobProvider:HomePage")
        else:
            return render(request,'Guest/Login.html',{'msg':"Invalid Email Or Password"})
    else:
        return render(request,'Guest/Login.html')

def JobproviderRegistration(request):
    districtDatas = tbl_district.objects.all()
    if request.method == "POST":
        name = request.POST.get("txt_name")
        email = request.POST.get("txt_email")
        contact = request.POST.get("txt_contact")
        address = request.POST.get("txt_address")
        place = tbl_place.objects.get(id=request.POST.get("sel_place"))
        photo = request.FILES.get("file_photo")
        proof = request.FILES.get("file_proof")
        password = request.POST.get("txt_password")
        repassword = request.POST.get("txt_repassword")
        checkjobprovideremail=tbl_jobprovider.objects.filter(jobprovider_email=email).count()
        checkuseremail=tbl_user.objects.filter(user_email=email).count()
        if checkjobprovideremail > 0:
            return render(request,"Guest/JobproviderRegistration.html",{'msg':"Email Already Exited"})
        elif checkuseremail > 0:
            return render(request,"Guest/JobproviderRegistration.html",{'msg':"Email Already Exited"})
        else:
            if password == repassword :
                tbl_jobprovider.objects.create(jobprovider_name=name,jobprovider_email=email,jobprovider_contact=contact,jobprovider_address=address,jobprovider_photo=photo,jobprovider_proof=proof,jobprovider_password=password,place=place)
                return render(request,"Guest/JobproviderRegistration.html",{'msg':"Registration Successfull"})
            else:
                return render(request,"Guest/JobproviderRegistration.html",{'msg':"Password Mismatch"})
    else:
        return render(request,'Guest/JobproviderRegistration.html',{"districtDatas":districtDatas})
    


def ForgotPassword(request):
    if request.method == "POST":
        email = request.POST.get("txt_email")


        if tbl_user.objects.filter(user_email=email).exists():
            user = tbl_user.objects.get(user_email=email)
            request.session["fid"] = user.id

        elif tbl_jobprovider.objects.filter(jobprovider_email=email).exists():
            jobprovider = tbl_jobprovider.objects.get(jobprovider_email=email)
            request.session["gid"] = jobprovider.id

        else:
            return render(request, "Guest/ForgotPassword.html", {"msg": "Email not registered"})

        otp = random.randint(111111, 999999)
        request.session["otp"] = otp

        send_mail(
            'Forgot password OTP',
            f"Hello\n\nYour OTP is {otp}\n\nThanks\nD MARKET Team",
            settings.EMAIL_HOST_USER,
            [email],
        )

        return redirect("Guest:OTP")

    return render(request, "Guest/ForgotPassword.html")



def OTP(request):
    if request.method == "POST":
        inp_otp = int(request.POST.get("txt_otp"))
        if inp_otp == request.session["otp"]:
            return redirect("Guest:NewPassword")
        else:
            return render(request,"Guest/OTP.html",{"msg":"OTP Does not Matches..!!"})
    else:
        return render(request,"Guest/OTP.html")


def NewPassword(request):
    if request.method == "POST":
        new_pass = request.POST.get("txt_new_pass")
        con_pass = request.POST.get("txt_con_pass")

        if new_pass != con_pass:
            return render(request, "Guest/NewPassword.html", {"msg": "Passwords do not match"})

        if "fid" in request.session:
            user = tbl_user.objects.get(id=request.session["fid"])
            user.user_password = new_pass
            user.save()

            del request.session["fid"]
            del request.session["otp"]

            return render(request, "Guest/NewPassword.html", {"msg1": "User password updated successfully"})

        elif "gid" in request.session:
            jobprovider = tbl_jobprovider.objects.get(id=request.session["gid"])
            jobprovider.jobprovider_password = new_pass
            jobprovider.save()

            del request.session["gid"]
            del request.session["otp"]

            return render(request, "Guest/NewPassword.html", {"msg1": "Job provider password updated successfully"})

        else:
            return render(request, "Guest/NewPassword.html", {"msg": "Session expired"})

    return render(request, "Guest/NewPassword.html")
