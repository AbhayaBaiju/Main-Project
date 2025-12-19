from django.urls import path
from Admin import views
app_name="Admin"
urlpatterns=[
    path('District/',views.District, name="District"),
    path('deletedistrict/<int:did>',views.DeleteDistrict,name="DeleteDistrict"),
    path('editdistrict/<int:eid>',views.EditDistrict,name="EditDistrict"),
   

    path('Category/',views.Category, name="Category"),
    path('deletecategory/<int:cid>',views.DeleteCategory,name="DeleteCategory"),
    path('editcategory/<int:eid>',views.EditCategory,name="EditCategory"),

    path('Place/',views.Place, name="Place"),
    path('deleteplace/<int:did>',views.DeletePlace,name="DeletePlace"),
    path('editplace/<int:eid>',views.EditPlace,name="EditPlace"),

    path('Subcategory/',views.Subcategory, name="Subcategory"),
    path('deletesubcategory/<int:did>',views.DeleteSubcategory,name="DeleteSubcategory"),
    path('editsubcategory/<int:eid>',views.EditSubcategory,name="EditSubcategory"),

    path('AdminRegistration/',views.AdminRegistration, name="AdminRegistration"),
    path('deleteadmin/<int:did>',views.DeleteAdmin,name="DeleteAdmin"),

    path('UserList/',views.UserList, name="UserList"),

    path('ViewComplaint/',views.ViewComplaint,name="ViewComplaint"),

    path('Reply/<int:eid>',views.Reply,name="Reply"),
    
    path('JobType/',views.JobType,name="JobType"),
    path('DeleteJobType/<int:did>',views.DeleteJobType,name="DeleteJobType"),

    path('JobCategory/',views.JobCategory,name="JobCategory"),
    path('DeleteJobCategory/<int:did>',views.DeleteJobCategory,name="DeleteJobCategory"),
    
    path('Qualification/',views.Qualification,name="Qualification"),
    path('DeleteQualification/<int:did>',views.DeleteQualification,name="DeleteQualification"),

    path('JobproviderVerification/',views.JobproviderVerification,name="JobproviderVerification"),
    path('Accept/<int:aid>',views.Accept,name="Accept"),
    path('Reject/<int:rid>',views.Reject,name="Reject"),
    path('Feedback/',views.Feedback,name='Feedback'),

    path('HomePage/',views.HomePage,name="HomePage"),

]