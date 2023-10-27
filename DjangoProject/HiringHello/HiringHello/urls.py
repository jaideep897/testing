"""
URL configuration for HiringHello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.get,name='form'),
    path('saveenquiry/',views.saveEnquiry,name='saveEnquiry') ,
    path('candidate_list/',views.show,name='form'),
    path('candidate_list/delete//<int:id>',views.Delete,name='delete'),
    path('candidate_list/update/<int:id>',views.Update_record,name='update'),
    path('update/updated/<int:id>',views.updated,name='updated'),
    path('company/',views.company,name='company'),
    path('company_list/',views.company_show,name='company_form'),
    path('company_list/company_Delete/<int:id>',views.company_Delete,name='company_Delete'),
    path('company_list/company_Update_record/<int:id>',views.company_Updating_record,name='company_Update_record'),
    path('company_list/company_Updated/<int:id>',views.company_Updating,name='company_updated'),
    path('Technology/',views.Technology,name='Technology'),
    path('technology_show/',views.technology_show,name='technology_show'),
    path('technology_show/technology_Delete/<int:id>',views.technology_Delete,name='technology_Delete'),
    path('technology_show/technology_Updating_record/<int:id>',views.technology_Updating_record,name='technology_Updating_record'),
    path('technology_show/technology_Updating/<int:id>',views.technology_Updating,name='technology_Updating'),
    path('job/',views.job,name='job'),
    path('view-job/',views.view,name='view-job'),
    path('Add-job/',views.Add_Job,name='Add-job'),


    path('company_list/view-details/<int:id>',views.view_detail,name='view-details'),


    
 
   




    




]
