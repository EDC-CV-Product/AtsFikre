"""ATS_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from ATS_Project import settings
from ATS_APP import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static

from ATS_APP.models import *

from ATS_APP.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/',views.UserApiView.as_view(),name="Applicant(GET)"),
    path('users/<int:users>',views.userdetailView.as_view(),name="User search by thier DI"),
    #Url for search query paramter string in the URL
    path('users/by_email',get_user_by_email,name="User Detail Using Email"),
    path('users/search_users',search_users,name="Search User By Names"),


    path('User_Roles/',views.UserRoleApiView.as_view(),name="User Role"),
    path('User_Roles/<int:User_Roles>',views.userroledetailView.as_view(),name="User Role Detail View"),
    path('User_Roles/get_by_id',get_by_id,name="User Role Using id"),
    

    path('Roles/',views.RoleApiView.as_view(),name="Role"),
    path('Roles/<int:Roles>',views.roledetailView.as_view(),name="Role Detail View"),


    path('Skill_Sets/',views.SkillsetApiView.as_view(),name="Skill"),
    path('Skill_Sets/<int:Skill_Sets>',views.skilldetailView.as_view(),name="Skill Detail View"),


    path('job_platform/',views.JobPlatformApiView.as_view(),name="Job Platform"),
    path('job_platform/<int:job_platform>',views.jobplatdetailView.as_view(),name="Job Platforms Detail View"),


    path('Companys/',views.CompanyApiView.as_view(),name="Company"),
    path('Companys/<int:Companys>',views.CompanydetailView.as_view(),name="Company Detail View"),

    path('applicant_cvs/',views.applicant_cvApiView.as_view(),name="Applicant Cv"),
    path('applicant_cvs/<int:applicant_cvs>',views.Applicant_cvdetailView.as_view(),name="applicant Cv Detail View"),

    path('Experiences/',views.ExperianceApiView.as_view(),name="Experiance"),
    path('Experiences/<int:Experiences>',views.ExperiancedetailView.as_view(),name="Experiance Detail View"),

    path('Educations/',views.EducationApiView.as_view(),name="Education"),
    path('Educations/<int:Educations>',views.EducationdetailView.as_view(),name="Education Detail View"),

    path('Jobs/',views.JobApiView.as_view(),name="Job"),
    path('Jobs/<int:Jobs>',views.jobdetailView.as_view(),name="Job Detail View"),
    path('Jobs/get_jobs_by_job_position',get_jobs_by_job_position,name="Jobs Detail Detail by  Using Job Position"),
  
    
    
    path('job_categorys/',views.JobCategoryApiView.as_view(),name="Job Category"),
    path('job_categorys/<int:job_categorys>',views.job_categorydetailView.as_view(),name="Job Category Detail View"),

    
    path('Applications/',views.ApplicationApiView.as_view(),name="Application"),# to Get Whole Data From The Database Table
    path('Applications/<int:Applications>',views.ApplicationdetailView.as_view(),name="Application Detail View"),# to searrch by Spesfic Parameter
    #to Return Applications using User_iD
    path('Applications/get_application_by_user_id',get_application_by_user_id,name="Application Detail Detail by User_ID"),

    #get All Applicant Document from DAtabase Table
    path('Applicant_Documents/',views.Applicant_DocumentApiView.as_view(),name="Applicant Document(GET)"),
    path('Applicant_Documents/<int:Applicant_Documents>',views.Applicant_DocumentdetailView.as_view(),name="Applicant(GET)"),
    #get Appliccant Document by using Certaim Parameter
    path('Applicant_Documents/get-by_user_id',usered,name="Applicant Detail View"),


    
    path('candidate_Evaluations/',views.Candidate_EvaluationApiView.as_view(),name="Candidate Evaluation"),
    path('candidate_Evaluations/<int:candidate_Evaluations>',views.CandidateEvaluationdetailView.as_view(),name="Candidate Evaluation Detail View"),
    # path to return candidate detail using job ID
    path('candidate_Evaluations/get_candidate_by_job_id',get_candidate_by_job_id,name="Candidate Detail by Job_ID"),

    path('Job_Description_Documents/',views.Job_Description_DocumentApiView.as_view(),name="Job Category"),
    path('Job_Description_Documents/<int:Job_Description_Documents>',views.JobDiscriptiondetailView.as_view(),name="Job Category Detail View"),

    path('applicantScore/get_applicant_score',get_applicant_score, name="Applicant Score"),

    path('JobsPage/', views.JobsPage.as_view(),name="JobsPage"),
    path('usersPage/', views.UsersPage.as_view(), name="UsersPage"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
