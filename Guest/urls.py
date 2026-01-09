from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns=[
    path('',views.index, name="index"),

    path('UserRegistration/',views.UserRegistration, name="UserRegistration"),
    path('AjaxPlace/',views.AjaxPlace,name="AjaxPlace"),
    path('Login/',views.Login,name="Login"),
    path('JobproviderRegistration/',views.JobproviderRegistration,name="JobproviderRegistration"),
    path('ForgotPassword/',views.ForgotPassword,name="ForgotPassword"),
    path('NewPassword/',views.NewPassword,name="NewPassword"),
    path('OTP/',views.OTP,name="OTP"),

]