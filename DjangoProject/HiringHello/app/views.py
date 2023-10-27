from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from.models import companymodel,companydetail,technology_list, job_list
from django.views import View 
from django.urls import reverse
from django.template import loader
from .forms import NewACCForm
from django.contrib import messages



def get(request):
   
    return render(request,'hello_hiring.html')



def view(request):
    data=job_list.objects.all()
    return render(request,'hello_hiring.html',{"messages":data})


# Create your views here.
def saveEnquiry(request):
    
    if request.method=='POST':
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        DOB=request.POST.get('DOB')
        CompanyName=request.POST.get('CompanyName')
        currentposition=request.POST.get('Currentposition')
        Experience=request.POST.get('Experience')
        CTC=request.POST.get('CTC')
        ECTC=request.POST.get('ECTC')
        Notice=request.POST.get('Notice')
        JobLocation=request.POST.get('job')
        source=request.POST.get('Source')
        CommunicationRating=request.POST.get('CommunicationRating')
        CV=request.POST.get('CV')
        Feedback=request.POST.get('Feedback')
        
        
        myuser=companymodel(
            name=name,
            contact=contact ,
            DOB=DOB, 
            CompanyName=CompanyName,
            currentposition=currentposition,
            Experience=Experience,
            CTC=CTC, ECTC=ECTC, 
            Notice=Notice, 
            JobLocation=JobLocation,
            source=source ,
            CommunicationRating=CommunicationRating ,
            CV=CV ,Feedback=Feedback
            )
        myuser.save()

        return render(request,'hello_hiring.html')
    return render(request,'Detail.html')

def show(request):
    data=companymodel.objects.all()
    for i in data:
    #   if data.null():
    #        return render("")
     return render(request,'candidate.html',{"messages":data})

def Delete(request,id):
    print(id)
    a=companymodel.objects.get(id=id)
    a.delete()
    return redirect ( '/candidate_list' )

# def Update(request,id):
#     a=companymodel.objects.get(id=id)
#     template=loader.get_template('detail.html')
#     context={
#         'a':a:
#     }

def Update_record(request, id):
   mem=companymodel.objects.get(id=id)
   return render (request, 'update.html',{'mem':mem})

def updated(request,id):
    name=request.POST['name']
    contact=request.POST['contact']
    DOB=request.POST['DOB']
    CompanyName=request.POST['CompanyName']
    currentposition=request.POST['Currentposition']
    Experience=request.POST['Experience']
    CTC=request.POST['CTC']
    ECTC=request.POST['ECTC']
    Notice=request.POST['Notice']
    JobLocation=request.POST['job']
    source=request.POST['Source']
    CommunicationRating=request.POST['CommunicationRating']
    CV=request.POST['CV']
    Feedback=request.POST['Feedback']

    member = companymodel.objects.get(id=id)
    member.name=name
  
    member.contact=contact
    member.CompanyName=CompanyName
    member.DOB=DOB
    member.currentposition=currentposition
    member.Experience=Experience
    member.CTC=CTC
    member.ECTC=ECTC
    member.Notice=Notice
    member.JobLocation=JobLocation
    member.source=source 
    member.CommunicationRating=CommunicationRating 
    member.CV=CV 
    member.Feedback=Feedback
    member.save()
    return HttpResponseRedirect('/')
   

#company detail starting
def company(request):
    if request.method=='POST':
        Company_Name=request.POST.get('name')
        contact=request.POST.get('contact')
        Email=request.POST.get('Company_E-Mail')
        source=request.POST.get('Source')
        city=request.POST.get('City')
        address=request.POST.get('address')
        website=request.POST.get('Company_Website')
        print(Company_Name,contact,Email,source,city,address,website)
        
        companyuser=companydetail(
          Company_Name=Company_Name,
          contact=contact ,
          Email=Email,
          source=source,
          city=city,
          address=address,
          website=website,
        )
       
        companyuser.save()
        print(companyuser)

        return render(request,'hello_hiring.html') 
    return render(request,'company.html')

def company_show(request):
    data=companydetail.objects.all()
    for i in data:
    #   if data.null():
    #        return render("")
     return render(request,'company_data.html',{"messages":data})
    

def company_Delete(request,id):
    print(id)
    a=companydetail.objects.get(id=id)
    a.delete()
    return redirect ( '/company_list' )


    
def company_Updating_record(request, id):
    mem=companydetail.objects.get(id=id)
    return render (request, 'company_update.html',{'mem':mem})

def company_Updating(request,id):
    Company_Name=request.POST['name']
    contact=request.POST['contact']
    Email=request.POST['Company_E-Mail']
    source=request.POST['Source']
    city=request.POST['City']
    address=request.POST['address']
    website=request.POST['Company Website']



    member = companydetail.objects.get(id=id)

    member.Company_Name=Company_Name
    member.contact=contact
    member.Email=Email
    member.source=source
    member.city=city
    member.address=address
    member.website=website
    member.save()
    return HttpResponseRedirect('/')

# technology list start

def Technology(request):
     if request.method == 'POST':
         Technology_Name=request.POST.get('Technology_Name')
         if technology_list.objects.filter(Technology_Name=Technology_Name).exists():
             return HttpResponse('<h1> This value already exist!! <br> <a href="http://127.0.0.1:8000/"> Home</a>')
         else:
             technology_list.objects.create(Technology_Name=Technology_Name)
             return redirect('/')
         
     else:
         return render(request,'technology_popup.html')
         
    # print('jaideep')
    # if request.method=='POST':
    #     Technology_Name=request.POST.get('technology')
    #     t=technology_list( Technology_Name=Technology_Name  )    
    
    #     t.save()
  
    # return render(request,'technology_popup.html')

    

# def Technology(request):
#     if request.method == 'POST':
#         form = technology_list(request.POST)
#         if form.is_valid():
#             # Handle valid form submission
#             # ...
#             pass
#         else:
#             form = technology_list()

#     return render(request, 'technology_popup.html', {'form': form})

# def Technology(request):
#     if request.method=='POST':
#         Technology_Name = NewACCForm(request.POST)
#         if Technology_Name.is_valid():
#             Technology_Name .save()
#             messages.success(request,"The New User is save !")
#         else:
#             messages.error(request, "Was not possible to save the user")
#     return render(request,'technology_popup.html')

def technology_show(request):
    data=technology_list.objects.all()
    return render(request,'technology.html',{"messages":data})

def technology_Delete(request,id):
    print(id)
    a=technology_list.objects.get(id=id)
    a.delete()  
    return redirect ('/technology_show')

def technology_Updating_record(request, id):
    tec=technology_list.objects.get(id=id)
    return render (request, 'technology_update.html',{'tec':tec})


def technology_Updating(request,id):
    
    Technology_Name=request.POST['technology']
    member = technology_list.objects.get(id=id)
    member.Technology_Name=Technology_Name
    member.save()
    return HttpResponseRedirect('/')


def job(request):
    if request.method=='POST':
        Company_Name=request.POST.get('name')
        post_date=request.POST.get('Postdate')
        technology=request.POST.get('Technology')
        description=request.POST.get('Discription')
        salary_LPA=request.POST.get('salary')
        post_name=request.POST.get('postname')
        experience_required=request.POST.get('experience')
        print(Company_Name,post_date,technology,description,salary_LPA,post_name,experience_required)
        
        companyuser=job_list(
          Company_Name=Company_Name,
          post_date=post_date ,
          technology=technology,
          description=description,
          salary_LPA=salary_LPA,
          post_name=post_name,
          experience_required=experience_required,
        )
       
        companyuser.save()
        print(companyuser)

         
    return render(request,'add_job.html')
def Add_Job(request):
    if request.method=='POST':
        Company_Name=request.POST.get('name')
        post_date=request.POST.get('Postdate')
        technology=request.POST.get('Technology')
        description=request.POST.get('Description')
        salary_LPA=request.POST.get('salary')
        post_name=request.POST.get('postname')
        experience_required=request.POST.get('experience')
        print(Company_Name,post_date,technology,description,salary_LPA,post_name,experience_required)
        
        companyuser=job_list(
          Company_Name=Company_Name,
          post_date=post_date ,
          technology=technology,
          description=description,
          salary_LPA=salary_LPA,
          post_name=post_name,
          experience_required=experience_required,
        )
       
        companyuser.save()
        print(companyuser)

         
    return render(request,'add_job.html')

# def job_show(request):
#     data=job_list.objects.all()
#     for i in data:
#     #   if data.null():
#     #        return render("")
#      return render(request,'hello_hiring.html',{"messages":data})



# def your_view(request):
#     filtered_data = companydetail.objects.filter(your_criteria)  # Add your filtering criteria here
#     return render(request, 'company_data.html', {'filtered_data': filtered_data})

def view_detail(request,id):
   
    a=companydetail.objects.filter(id=id)
    for i in a:
       
       return render ( request,'view_details.html',{'view':a})
    




              
