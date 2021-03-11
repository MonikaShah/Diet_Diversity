from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import bulkreg,StudentForm,MukhyaSevikaForm,AnganwadiWorkerForm,SchoolForm,SchoolCoordinatorForm,MentorForm,ProjectManagerForm,Form,AnemicPregnantWomanForm,ConcentForm,NutriGardenExpertForm,SMChildParentsRegisterForm,PrincipalInvestigatorsForm,WebGISExpertForm,NutritionExpertForm,AnemicLactatingMotherForm,AnemicAdolescentGirlForm,SMChildForm,SchoolStudentParentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from .models import bulk_reg,Mentor,MukhyaSevika,AnganwadiWorkersRegister,Student,School,SchoolCoordinator,ProjectManager,User,AnemicPregnantWoman,ConcentForm,NutriGardenExpert,SMChildParentsRegister,PrincipalInvestigators,WebGISExpert,NutritionExpert,AnemicLactatingMother,AnemicAdolescentGirl,SMChild,SchoolStudentParent
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from tablib import Dataset
from django.http import JsonResponse
import openpyxl
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from .resources import bulkResource
from django.http import HttpResponse
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
import hashlib
from .encryption_util import encrypt, decrypt
# Create your views here.
def register(request):
    if request.method== "POST":
        profile_form=SchoolForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        # contact = request.POST['contact']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                print('Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request,"Email address Taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                if profile_form.is_valid():

                    user.save()
                    profile= profile_form.save(commit=False)
                    profile.user=user
                    profile.save()
                    
                    messages.info(request,"User created")
                    user= authenticate(username=username, password= password1)
                    login(request,user)
                    print('user created')
                    return redirect('login')


        else:
            messages.info(request,"password does not match")

            print('password does not match.')
            return redirect('register')
        return redirect('register')

    else:
        profile_form= SchoolForm()
        return render(request, "register.html",{"profile_form":profile_form})

def nutrition_expert(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=NutritionExpertForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='nutrition_expert') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form= NutritionExpertForm()
    return render(request, "nutri_expert_register.html",{"profile_form":profile_form,"form":form})
def proj_manager(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=ProjectManagerForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='project_manager') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form= ProjectManagerForm()
    return render(request, "proj_manager_register.html",{"profile_form":profile_form,"form":form})





def school(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=SchoolForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='school') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form()
        profile_form= SchoolForm()
    return render(request, "school_register.html",{"profile_form":profile_form,"form":form})

def school_coordinator_register(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=SchoolCoordinatorForm(request.POST,request.FILES)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='school_coordinator') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form()
        profile_form= SchoolCoordinatorForm()
    return render(request, "school_coordinator_register.html",{"profile_form":profile_form,"form":form})
def student(request):
               
   

    if request.method== "POST":
        form= Form(request.POST)
        # print(form)
        profile_form=StudentForm(request.POST,request.FILES)
        
        # print('not valid')
        if form.is_valid() and profile_form.is_valid():
            instance = form.save(commit=False)
            profile=profile_form.save(commit=False)
            # instance.first_name=f.encrypt(b"form.cleaned_data['first_name']")
            # instance.last_name=f.encrypt(b"form.cleaned_data['last_name']")
            # instance.email=f.encrypt(b"form.cleaned_data['email']")
            # instance.username=f.encrypt(b"form.cleaned_data['username']")
            # profile.contact=f.encrypt(b"form.cleaned_data['contact']")
            instance.save()
            print(instance.first_name)
            
            profile.user=instance
            print("working")
            profile.save() 
            my_group = Group.objects.get(name='student') 
            my_group.user_set.add(instance)
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
    
            print('user created')
            return redirect('/personal')
    else:
        form= Form()
        profile_form= StudentForm()
    return render(request, "student_register.html",{"profile_form":profile_form,"form":form})

def mukhya_sevika_register(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=MukhyaSevikaForm(request.POST,request.FILES)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='mukhya_sevika') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form= MukhyaSevikaForm()
    return render(request, "mukhya_sevika_register.html",{"profile_form":profile_form,"form":form})

def anganwadi_workers_register(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=AnganwadiWorkerForm(request.POST,request.FILES)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='anganwadi_worker') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form= AnganwadiWorkerForm()
    return render(request, "anganwadi_workers_register.html",{"profile_form":profile_form,"form":form})



def anemic_pregnant_woman_registration(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=AnemicPregnantWomanForm(request.POST,request.FILES)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='anemic_pregnant_woman') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login')
    else:
        form= Form(request.POST)
        profile_form= AnemicPregnantWomanForm()
    return render(request,"anemic_pregnant_woman_register.html",{"profile_form":profile_form,"form":form})
    

def sam_mam_child_register(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form= SMChildForm(request.POST,request.FILES)
        print(profile_form)
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='sam_mam_child') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form= SMChildForm()
    return render(request,"sam_mam_child_register.html",{"profile_form":profile_form,"form":form})

def SMChildParentsRegister(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form= SMChildParentsRegisterForm(request.POST)
        print(profile_form)
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='parents') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form= SMChildParentsRegisterForm()
    return render(request,"sam_mam_parent_registration.html",{"profile_form":profile_form,"form":form})


def concentform(request):
    if request.method == 'POST':
        print("after post")
        form = ConcentForm(request.POST)
        print(form)
        if form.is_valid():
                form.save()
                print("saved")
        return render(request,'concentform.html')  

    else:
        form = ConcentForm()
    return render(request,'concentform.html')
    
def nutri_garden_expert(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=NutriGardenExpertForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='nutrigarden_expert') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form=  NutriGardenExpertForm()
    return render(request, "nutri_garden_expert.html",{"profile_form":profile_form,"form":form}) 

def mentor_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_pm.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            id=data[6]
            print(id)
            new=encrypt(data[6])
            print(new)
            print(decrypt(new))
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                
                value.save()
                my_group = Group.objects.get(name='school_coordinator') 
                my_group.user_set.add(value)
                contact=SchoolCoordinator(uid=data[6],contact=encrypt(data[7]),schoolname=encryprt(data[8]),personaladdress=data[9],birthdate=data[10],age=data[11],schooladdress=data[12],schoolcontact=data[13],education=data[14],occupation=data[15],annualincome=data[16],profile_photo=data[17],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"after_login copy.html")
    else:
        return render(request,"bulk_reg_pm.html")






# def nutri_garden_expert_bulk(request):
#     if request.method== "POST":
#         bulk_resource = bulkResource()
#         dataset = Dataset()
#         bulk =request.FILES['myFile']
#         print(bulk)
#         if not bulk.name.endswith('xlsx'):
#             messages.info(request,'wrong format')
#             return render(request, "bulk_reg_nge.html")

#         imported_data = dataset.load(bulk.read(),format='xlsx')
#         print(imported_data)
#         user=User.objects.all()
#         for data in imported_data:
#             if User.objects.filter(username=data[3]).exists():
#                 messages.info(request,"Username already entered")
            
            
#             else:
#                 value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
#                 value.save()
#                 my_group = Group.objects.get(name='nutrigarden_expert') 
#                 my_group.user_set.add(value)
#                 contact=NutriGardenExpert(contact=data[6])
#                 contact.save()
#                 messages.info(request,"User created")
#                 print('user created')

#                 stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
#                 print(stuff_in_string)
#                 # email=i.email }}
#                 send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
#                     [data[4]], fail_silently=False)        
#                 # messages.info(request,"data entered")       
#         return render(request,"bulk_reg_nge.html")
#     else:
#         return render(request,"bulk_reg_nge.html")
    
def school_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_s.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='school') 
                my_group.user_set.add(value)
                contact=School(contact=data[6],name=data[7],institute=data[8],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_s.html")
    else:
        return render(request,"bulk_reg_s.html")
    
def student_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_stu.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='student') 
                my_group.user_set.add(value)
                contact=Student(uid=data[6],weight=data[7],weightunit=data[8],height=data[9],heightunit=data[10],bmi=data[10],waist=data[11],waistunit=data[12],hip=data[13],hipunit=data[14],whratio=data[15],whratioderived=data[16],nutirleader=data[17],schoolname=data[18],schoolcordinatorincharge=data[19],schooladdress=data[20],schoolcontactinformation=data[21],contact=data[22],uploaded_photo=data[23],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_stu.html")
    else:
        return render(request,"bulk_reg_stu.html")

def anganwadi_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_aw.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group =  Group.objects.get(name='anganwadi_worker') 
                my_group.user_set.add(value)
                contact=AnganwadiWorker(uid=data[6],contact=data[7],birthdate=data[8],age=data[9],education=data[10],occupation=data[11],annualincome=data[12],anganwadiname=data[13],anganwadiaddress=data[14],ICDSname=data[15],ICDScenteraddress=data[16],ICDScontact=data[17],profile_photo=data[18],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_aw.html")
    else:
        return render(request,"bulk_reg_aw.html")

def mukhyasevika_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_ms.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='mukhya_sevika') 
                my_group.user_set.add(value)
                contact=MukhyaSevika(uid=data[6],anganwadinumber=data[7],contact=data[8],birthdate=data[9],age=data[10],education=data[11],occupation=data[12],annualincome=data[13],ICDSname=data[14],ICDScenteraddress=data[15],ICDScontact=data[16],profile_photo=data[17],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_ms.html")
    else:
        return render(request,"bulk_reg_ms.html")

def headmentor_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_hm.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='mentor') 
                my_group.user_set.add(value)
                contact=Mentor(uid=data[6],birthdate=data[7],age=data[8],contact=data[9],address=data[10],education=data[11],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_hm.html")
    else:
        return render(request,"bulk_reg_hm.html")



def adolescent_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_adolescent.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='adolescent_girl') 
                my_group.user_set.add(value)
                contact=AnemicAdolescentGirl(uid=data[6],birthdate=data[7],age=data[8],personalcontact=data[9],ICDSname=data[10],ICDScenteraddress=data[11],ICDScentercontact=data[12],occupation=data[13],education=data[14],annualincome=data[15],weight=data[16],weightunit=data[17],height=data[18],heightunit=data[17],bmi=data[18],waist=data[19],waistunit=data[20],hip=data[21],hipunit=data[22],whratio=data[23],whratioderived=data[24],foodhabbits=data[25],uploaded_photo=data[26],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_adolescent.html")
    else:
        return render(request,"bulk_reg_adolescent.html")
    
def sm_parent_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_parent.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='parents') 
                my_group.user_set.add(value)
                contact=Parent(uid=data[6],mothername=data[7],fathername=data[8],motherbirthdate=data[9],fatherbirthdate=data[10],motherage=data[11],fatherage=data[12],personalcontact=data[13],ICDSname=data[14],ICDScenteraddress=data[15],ICDScentercontact=data[16],occupation=data[17],education=data[18],annualincome=data[19],cuid=data[20],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_parent copy.html")
    else:
        return render(request,"bulk_reg_parent copy.html")

def school_parent_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_parent.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='parents') 
                my_group.user_set.add(value)
                contact=Parent(uid=data[6],contact=data[7],schoolname=data[8],personaladdress=data[9],birthdate=data[10],age=data[11],schooladdress=data[12],schoolcontact=data[13],education=data[14],occupation=data[15],annualincome=data[16],schoolcoordinatorincharge=data[17],foodhabbits=data[18],profile_photo=data[19],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_parent.html")
    else:
        return render(request,"bulk_reg_parent.html")
def lactatingwoman_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_pregnant.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='anemic_lactating_mother') 
                my_group.user_set.add(value)
                contact=AnemicLactatingMother(uid=data[6],birthdate=data[7],age=data[8],personalcontact=data[9],ICDSname=data[10],ICDScenteraddress=data[11],ICDScentercontact=data[12],occupation=data[13],education=data[14],annualincome=data[15],weight=data[16],weightunit=data[17],height=data[18],heightunit=data[17],bmi=data[18],waist=data[19],waistunit=data[20],hip=data[21],hipunit=data[22],whratio=data[23],whratioderived=data[24],foodhabbits=data[25],uploaded_photo=data[26],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_pregnant copy.html")
    else:
        return render(request,"bulk_reg_pregnant copy.html")
def anemicwoman_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_pregnant.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='anemic_pregnant_woman') 
                my_group.user_set.add(value)
                contact=AnemicPregnantWoman(uid=data[6],birthdate=data[7],age=data[8],personalcontact=data[9],ICDSname=data[10],ICDScenteraddress=data[11],ICDScentercontact=data[12],occupation=data[13],education=data[14],annualincome=data[15],weight=data[16],weightunit=data[17],height=data[18],heightunit=data[17],bmi=data[18],waist=data[19],waistunit=data[20],hip=data[21],hipunit=data[22],whratio=data[23],whratioderived=data[24],foodhabbits=data[25],uploaded_photo=data[26],feedback=data[27],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_pregnant.html")
    else:
        return render(request,"bulk_reg_pregnant.html")

def nutriexpert_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_nutriexp.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='nutri_garden_expert') 
                my_group.user_set.add(value)
                contact=NutriGardenExpert(uid=data[6],birthdate=data[7],age=data[8],contact=data[9],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_nutriexp.html")
    else:
        return render(request,"bulk_reg_nutriexp.html")

def principal_investigator_register(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form= PrincipalInvestigatorsForm(request.POST)
        print(profile_form)
      
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='principal_investigator') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form= PrincipalInvestigatorsForm()
    return render(request, "principal_investigator_register.html",{"profile_form":profile_form,"form":form})

def webgis_expert_register(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=  WebGISExpertForm(request.POST)
        print(profile_form)
      
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='webgis_expert') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form=  WebGISExpertForm()
    return render(request,"webgis_expert_register.html",{"profile_form":profile_form,"form":form})
   
def mentor_registration(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form= MentorForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='mentor') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/mentor_register/')
    else:
        form= Form(request.POST)
        profile_form= MentorForm()
    return render(request,"mentor_register.html",{"profile_form":profile_form,"form":form})
    
def anemic_adolescent_girl_register(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=  AnemicAdolescentGirlForm(request.POST,request.FILES)
        print(profile_form)
      
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='adolescent_girl') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form=  AnemicAdolescentGirlForm()
    return render(request,"anemic_adolescent_girl_register.html",{"profile_form":profile_form,"form":form})
   
def anemic_lactating_mother_resgiter(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=  AnemicLactatingMotherForm(request.POST,request.FILES)
        print(profile_form)
      
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='anemic_lactating_mother') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form=  AnemicLactatingMotherForm()
    return render(request,"anemic_Lactating_mother_register.html",{"profile_form":profile_form,"form":form})
   
def school_student_parent_register(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=SchoolStudentParentForm(request.POST,request.FILES)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='parents') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form()
        profile_form= SchoolStudentParentForm()
    return render(request, "school_student_parent_register.html",{"profile_form":profile_form,"form":form})