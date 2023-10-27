from django.contrib import admin
from app.models import companymodel, companydetail,technology_list,job_list
class companyadmin(admin.ModelAdmin):
    list_display=(
        'name','contact',
        'DOB','CompanyName',
        'currentposition','Experience',
        'CTC','ECTC','Notice',
        'JobLocation','source',
        'CommunicationRating','CV',
        'Feedback')
admin.site.register(companymodel,companyadmin)  


class companydetailadmin(admin.ModelAdmin):
    list_display=(
        'Company_Name','contact','Email','source','city','address','website',
        )
admin.site.register(companydetail,companydetailadmin)

class technology_listadmin(admin.ModelAdmin):
    list_di=(
        'Technology_Name'
    )

admin.site.register(technology_list,technology_listadmin)

class job_listadmin(admin.ModelAdmin):
    list_display=(
        'Company_Name','post_date','technology','description','salary_LPA','post_name','experience_required',
        )
admin.site.register(job_list,job_listadmin)
