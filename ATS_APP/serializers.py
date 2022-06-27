from cProfile import label
from dataclasses import field, fields
from typing import ItemsView
from rest_framework import serializers

from ATS_APP.models import user
from ATS_APP.models import Applicant_Document, Application, Company, Education, Experience, Job, Job_Description_Document, Role, Skill_Set, User_Role, applicant_cv, candidate_Evaluation, job_category, job_platforms

class UserSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(label="User ID:")
    first_name = serializers.CharField(label="First Name:")
    middle_name=serializers.CharField(label="Middle Name:")
    last_name = serializers.CharField(label="Last Name:")
    email = serializers.CharField(label="Email:")
    password = serializers.CharField(label="Password:")
    city=serializers.CharField(label="City:")
    phone=serializers.CharField(label="Phone:")
    country=serializers.CharField(label="Country:")
    class Meta: 
        model =user
        fields='__all__'
        extra_kwargs = {'password': {'write_only': True}}
class userdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields='__all__'

# User Role Serializer Starts Here

class UserRoleSerializer(serializers.ModelSerializer):
    role = serializers.CharField(label="Role:")
    user=serializers.CharField(label="User:")
    class Meta: 
        model =User_Role
        fields='__all__'
class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Role
        fields = ('role', 'user',)

# Role Serializer Starts Here

class RoleSerializer(serializers.ModelSerializer):
    name=serializers.CharField(label="Name:")

    class Meta: 
        model =Role
        fields='__all__'

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'

#  Skill Set Starts Here

class SkillsetSerializer(serializers.ModelSerializer):
    skill = serializers.CharField(label="skill:")
    #skill_level=serializers.CharField(label="skill_level:")
    applicant_cv=serializers.CharField(label="applicant_cv:")


    class Meta: 
        model =Skill_Set
        fields='__all__'
class SkillsetSerializer(serializers.ModelSerializer):


    class Meta:
        model = Skill_Set
        fields='__all__'

# Job Platform Starts Here

class jobplatformSerializer(serializers.ModelSerializer):
    code = serializers.CharField(label="code:")
    name=serializers.CharField(label="name:")
    description=serializers.CharField(label="description:")

    class Meta: 
        model =job_platforms
        fields='__all__'
class jobplatformSerializer(serializers.ModelSerializer):


    class Meta:
        model = job_platforms
        fields='__all__'

#  Company Starts Here

class CompanySerializer(serializers.ModelSerializer):
    code = serializers.CharField(label="code:")
    name=serializers.CharField(label="name:")
    description=serializers.CharField(label="description:")

    class Meta: 
        model =Company
        fields='__all__'

class CompanySerializer(serializers.ModelSerializer):


    class Meta:
        model = Company
        fields='__all__'

#  applicant_cv Starts Here

class Applicant_cvSerializer(serializers.ModelSerializer):
    #applicant_id = serializers.(label="date_created:")
    date_created=serializers.DateTimeField(label="gender:")
    gender=serializers.CharField(label="zip_code:")
    summary = serializers.CharField(label="country:")
    last_updated=serializers.DateTimeField(label="city:")
    zip_code=serializers.CharField(label="phone:")
    country=serializers.CharField(label="phone2:")
    city=serializers.CharField(label="zip_code:")
    phone = serializers.CharField(label="training_certification:")
    phone2=serializers.CharField(label="applicant_cv:")
    training_certification = serializers.CharField(label="training_certification:")
    applicant_cv=serializers.FileField(label="applicant_cv:")

    class Meta: 
        model =applicant_cv
        fields='__all__'

class Applicant_cvSerializer(serializers.ModelSerializer):
 

    class Meta:
        model = applicant_cv
        fields = '__all__'

# Experiance Starts Here

class ExperianceSerializer(serializers.ModelSerializer):
    organization = serializers.CharField(label="organization:")
    title=serializers.CharField(label="title:")
    begin_date=serializers.DateTimeField(label="begin_date:")
    end_date = serializers.DateTimeField(label="end_date:")
    applicant_cv=serializers.CharField(label="applicant_cv:")


    class Meta: 
        model =Experience
        fields='__all__'

class ExperianceSerializer(serializers.ModelSerializer):


    class Meta:
        model = Experience
        fields='__all__'
        

#  Education Starts Here

class EducationSerializer(serializers.ModelSerializer):
    institution_name = serializers.CharField(label="institution_name:")
    degree_obtained=serializers.DateTimeField(label="degree_obtained:")
    date_attended_from=serializers.DateTimeField(label="date_attended_from:")
    date_attended_to = serializers.DateTimeField(label="date_attended_to:")
    applicant_cv=serializers.CharField(label="applicant_cv:")


    class Meta: 
        model =Education
        fields='__all__'

class EducationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Education
        fields='__all__'


# Job Starts Here

class JobSerializer(serializers.ModelSerializer):
    description = serializers.CharField(label="description:")
    code=serializers.CharField(label="Code")
    date_published=serializers.DateTimeField(label="date_published:")
    job_deadline=serializers.DateTimeField(label="job_deadline:")
    number_of_vacancies = serializers.CharField(label="number_of_vacancies:")
    job_category=serializers.CharField(label="job_category:")
    job_position = serializers.CharField(label="job_position:")
    job_platform=serializers.CharField(label="job_platform:")
    organization_name=serializers.CharField(label="organization_name:")
    file = serializers.FileField(label="file:")

    class Meta: 
        model =Job
        fields='__all__'
   
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields='__all__'


# JobCategory Starts Here

class JobcategorySerializer(serializers.ModelSerializer):
     
    code=serializers.CharField(label="code:")
    name=serializers.CharField(label="name:")
    description = serializers.CharField(label="description:")


    class Meta: 
        model =job_category
        fields='__all__'
  

   
class JobcategorySerializer(serializers.ModelSerializer):
 

    class Meta:
        model = job_category
        fields='__all__'


# Application Starts Here

class ApplicationSerializer(serializers.ModelSerializer):
     
    date_of_application=serializers.DateTimeField(label="Date_of_Application:")
    job=serializers.CharField(label="job:")
    user = serializers.CharField(label="User:")
    application_status = serializers.CharField(label="Application_Status:")

    class Meta: 
        model =Application
        fields='__all__'
  
  
class ApplicationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Application
        fields = '__all__'


# Applicant_Document Starts Here

class ApplicatDocumentSerializer(serializers.ModelSerializer):
    name=serializers.CharField(label="Name:")
    document=serializers.FileField(label="Document:")
    url = serializers.CharField(label="URL:")
    last_updated = serializers.FileField(label="Last_Updated:")
    user = serializers.CharField(label="User:")


    class Meta: 
        model =Applicant_Document
        fields='__all__' 
  

   
class ApplicatDocumentSerializer(serializers.ModelSerializer):
    #tag = ApplicatDocumentSerializer()
    ## user = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Applicant_Document
        fields = ('applicant_document_id', 'name', 'url', 'document', 'user', 'last_updated')


# candidate_Evaluation Starts Here

class candidate_EvaluationSerializer(serializers.ModelSerializer):
     
    evaluation_notes=serializers.CharField(label="evaluation_notes:")
    job=serializers.CharField(label="job:")
    applicant = serializers.CharField(label="applicant:")
    evaluation_result = serializers.CharField(label="evaluation_result:")


    class Meta: 
        model =candidate_Evaluation
        fields='__all__'
  
  
class candidate_EvaluationSerializer(serializers.ModelSerializer):
    candidate_user = userdetailSerializer()
    class Meta:
        model = candidate_Evaluation
        fields='__all__'
   
"""class candidate_EvaluationSerializer(serializers.ModelSerializer):
 

    class Meta:
        model = candidate_Evaluation
        fields='__all__'"""


# Job_Discription Starts Here

class jobDiscriptionSerializer(serializers.ModelSerializer):
     
    name=serializers.CharField(label="name:")
    document=serializers.FileField(label="document:")
    last_updated = serializers.DateTimeField(label="last_updated:")
    job = serializers.CharField(label="job:")
  
    class Meta: 
        model =Job_Description_Document
        fields='__all__'
   
class jobDiscriptionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Job_Description_Document
        fields='__all__'



