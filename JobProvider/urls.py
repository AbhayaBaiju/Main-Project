from django.urls import path
from JobProvider import views
app_name="JobProvider"
urlpatterns=[
    path('HomePage/',views.HomePage, name="HomePage"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('Job/',views.Job,name="Job"),
    path('DeleteJob/<int:did>',views.DeleteJob,name="DeleteJob"),
    path('JobQualification/<int:jid>',views.JobQualification,name="JobQualification"),
    path('DeleteJobqualification/<int:did>',views.DeleteJobqualification,name="DeleteJobqualification"),
    path('ViewRequest/',views.ViewRequest,name="ViewRequest"),
    path('Accept/<int:aid>',views.Accept,name="Accept"),
    path('Reject/<int:rid>',views.Reject,name="Reject"),

    path('examinationdetails/<int:id>',views.examinationdetails,name='examinationdetails'),
    path('addquestions/<int:id>',views.addquestions,name='addquestions'),
    path('addoptions/<int:id>',views.addoptions,name='addoptions'),
    path('delopt/<int:id>/<int:did>',views.delopt,name='delopt'),


    path('myexam/',views.MyExam,name='MyExam'),
    path('viewexaminer/<int:id>',views.viewexaminer,name='viewexaminer'),
    path('ViewResult/<int:id>/<int:uid>',views.ViewResult,name='ViewResult'),
    path('Feedback/',views.Feedback,name='Feedback'),
    path('SendMail/<int:uid>/',views.SendMail,name="SendMail"),
    path('Logout/',views.Logout,name="Logout"),




]