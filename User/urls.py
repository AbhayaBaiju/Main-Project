from django.urls import path
from User import views
app_name="User"
urlpatterns=[
    path('HomePage/',views.HomePage, name="HomePage"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('Complaint/',views.Complaint,name="Complaint"),
    path('DeleteComplaint/<int:did>',views.DeleteComplaint,name="DeleteComplaint"),
    path('ViewJob/',views.ViewJob,name="ViewJob"),
    path('Request/<int:id>',views.Request,name="Request"),
    path('MyRequest/',views.MyRequest,name="MyRequest"),
    
    path('ViewExam/<int:id>',views.viewexam,name="ViewExam"),
    path('viewquestion/<int:id>',views.viewquestion,name='viewquestion'),
    path('ajaxexamanswer/',views.ajaxexamanswer,name='ajaxexamanswer'),
    path('ajaxtimer/',views.ajaxtimer,name='ajaxtimer'),
    path('successer/',views.successer,name='successer'),
    path('Feedback/',views.Feedback,name='Feedback'),
    path('Logout/',views.Logout,name="Logout"),

    path('AjaxSearch/',views.AjaxSearch,name="AjaxSearch"),


    
]
