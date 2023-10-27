from django.db import models
class companymodel(models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField(blank=True ,null=True)
    DOB=models.DateField()
    CompanyName=models.CharField(max_length=500)
    currentposition=models.CharField(max_length=300)
    Experience=models.CharField(max_length=300)
    CTC=models.IntegerField()
    ECTC=models.IntegerField()
    Notice=models.CharField(max_length=400)
    JobLocation=models.CharField(max_length=100)
    source=models.CharField(max_length=100)
    CommunicationRating=models.CharField(max_length=100)
    CV=models.FileField(upload_to='uploads/')
    Feedback=models.CharField(max_length=1000)

class companydetail(models.Model):
    Company_Name=models.CharField(max_length=50)
    contact=models.IntegerField(blank=True ,null=True)
    Email=models.EmailField(max_length=300)
    source=models.CharField(max_length=300)
    city=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    website=models.CharField(max_length=500)
    
class technology_list(models.Model):
    Technology_Name=models.CharField(max_length=100)
    
#it used when we didn't get the value in database and database show only object
    def __str__(self) -> str:
        return self.Technology_Name
class job_list(models.Model):
        Company_Name=models.CharField(max_length=50)
        post_date=models.DateField()
        technology=models.CharField(max_length=100)
        description=models.CharField(max_length=100)
        salary_LPA=models.IntegerField()
        post_name=models.CharField(max_length=300)
        experience_required=models.CharField(max_length=300)

# class view_details(models.Model):
#         Company_Name=models.CharField(max_length=50)
#         Company_Number=models.IntegerField(blank=True ,null=True)
#         company_Email=models.EmailField(max_length=300)
#         Company_Linkedin_URL=models.CharField(max_length=1000)
#         Company_Address=models.CharField(max_length=500)
#         Company_city=models.CharField(max_length=300)
#         Company_Website=models.CharField(max_length=300)
        

