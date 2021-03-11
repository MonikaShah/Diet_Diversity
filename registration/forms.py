from django import forms  
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.forms import UserCreationForm
import random
import string
from django.forms import Textarea
from bootstrap_datepicker_plus import DatePickerInput
from .models import bulk_reg,Mentor,MukhyaSevika,AnganwadiWorkersRegister,Student,School,SchoolCoordinator,ProjectManager,User,AnemicPregnantWoman,SMChildParentsRegister,ConcentForm,NutriGardenExpert,PrincipalInvestigators,WebGISExpert,NutritionExpert,AnemicLactatingMother,AnemicAdolescentGirl,SMChild,SchoolStudentParent
class Form(UserCreationForm):
    email=forms.EmailField(required=False)
    
    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)

        for fieldname in ['first_name','last_name','username','email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model=User
        fields=('first_name','last_name','username','email', 'password1', 'password2')
    def save(self, commit=True):
        user= super().save(commit=False)

        user.email= self.cleaned_data['email']

        if commit:
            user.save()
            print(user)
        return user 

# class bulkreg(forms.ModelForm):  
#     class Meta:  
#         model = bulk_reg  
#         fields = ['name','email','mobile','roles','from_date','to_date']  
#         widgets = {
#             'from_date':forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
#             'to_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
#         }
    


        
class ProjectManagerForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='PM'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    class Meta:
        model = ProjectManager
        fields = ('birthdate','age','contact','uid')
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), # default date-format %m/%d/%Y will be used
            
        }

class MentorForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='MT'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    class Meta:
        model = Mentor
        fields = ('birthdate','age','contact','address','education')


class SchoolCoordinatorForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='SCU'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))

    class Meta:
        model = SchoolCoordinator
        fields = ('contact','personaladdress','birthdate','age','schoolname','schooladdress','schoolcontact','education','occupation','annualincome','profile_photo','uid')
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('contact','name','institute',)

class StudentForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='STU'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    weight=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    weightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in kgs/lbs'}))
    height=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    heightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in feet/inches/cms/meters'}))
    waist=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    waistunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    hip=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    hipunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    
    class Meta:
        model = Student
        fields = ('birthdate','age','contact','nutrileader','schoolname','schoolcordinatorincharge','schooladdress','schoolcontactinformation','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','uploaded_photo','uid',)

class AnganwadiWorkerForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='ANW'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    class Meta:
        model = AnganwadiWorkersRegister
        fields = ('contact','birthdate','age','education','occupation','annualincome','anganwadiname','anganwadiaddress','ICDSname','ICDScenteraddress','ICDScontact','profile_photo','uid')
        # widgets = {
        #             'birthdate': DatePickerInput(format='%Y/%m/%d'),
        #          }
        
class MukhyaSevikaForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='MSU'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    class Meta:
        model = MukhyaSevika
        fields = ('anganwadinumber','contact','birthdate','age','education','occupation','annualincome','ICDSname','ICDScenteraddress','ICDScontact','profile_photo','uid')
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class SchoolStudentParentForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='STUP'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    class Meta:
        model = SchoolStudentParent
        fields = ('contact','schoolname','personaladdress','birthdate','age','schooladdress','schoolcontact','education','occupation','annualincome','schoolcoordinatorincharge','foodhabits','profile_photo','uid')
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class bulkreg(forms.ModelForm):  
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    class Meta:  
        model = bulk_reg  
        fields = ['name','mobile','birthdate']  
        widgets = {
            'birthdate':forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            # 'to_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
# class DocumentForm(forms.Form):
#     title=forms.CharField(max_length=150, required=False)
#     docfile = forms.FileField(
#         label='Select a file',
#         help_text='max. 42 megabytes'
#     )
class AnemicLactatingMotherForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='ALM'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    weight=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    weightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in kgs/lbs'}))
    height=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    heightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in feet/inches/cms/meters'}))
    waist=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    waistunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    hip=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    hipunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    class Meta:
        model = AnemicLactatingMother
        fields =  ['birthdate','age','personalcontact','ICDSname','ICDScenteraddress','ICDScentercontact','occupation','education','annualincome','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','foodhabits','uploaded_photo','uid'] 
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                  
        }
class AnemicAdolescentGirlForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='AAG'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    weight=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    weightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in kgs/lbs'}))
    height=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    heightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in feet/inches/cms/meters'}))
    waist=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    waistunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    hip=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    hipunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    
    class Meta:
        model = AnemicAdolescentGirl
        fields = ['birthdate','age','personalcontact','ICDSname','ICDScenteraddress','ICDScentercontact','occupation','education','annualincome','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','foodhabits','uploaded_photo','uid']
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                  
        }
class AnemicPregnantWomanForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='APW'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    weight=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    weightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in kgs/lbs'}))
    height=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    heightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in feet/inches/cms/meters'}))
    waist=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    waistunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    hip=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    hipunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    class Meta:
        model = AnemicPregnantWoman
        fields = ['birthdate','age','personalcontact','ICDSname','ICDScenteraddress','ICDScentercontact','occupation','education','annualincome','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','foodhabits','uploaded_photo','uid']
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                  
        }

class SMChildForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='SMC'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    weight=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    weightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in kgs/lbs'}))
    height=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    heightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in feet/inches/cms/meters'}))
    waist=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    waistunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    hip=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    hipunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    class Meta:
        model = SMChild
        fields = ['birthdate','age','personalcontact','ICDSname','ICDScenteraddress','ICDScentercontact','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','foodhabits','uploaded_photo','uid']
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                  
        }


class SMChildParentsRegisterForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='SMP'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    motherbirthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    fatherbirthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class1','placeholder':'yyyy/mm/dd'}))
    class Meta:
        model = SMChildParentsRegister
        fields =  ['mothername','fathername','motherbirthdate','fatherbirthdate','motherage','fatherage','personalcontact','ICDSname','ICDScenteraddress','ICDScentercontact','occupation','education','annualincome','cuid','uid'] 
        widgets = {
                    'motherbirthdate': DatePickerInput(format='%m/%d/%Y'), 
                    'fatherbirthdate': DatePickerInput(format='%m/%d/%Y'),
        }
class ConcentForm(forms.ModelForm):
    class Meta:
        model = ConcentForm
        fields = ['concent']
class NutriGardenExpertForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='NGE'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))

    class Meta:
        model = NutriGardenExpert
        fields = ['birthdate','age','contact','uid']
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), # default date-format %m/%d/%Y will be used
            
        }

class PrincipalInvestigatorsForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='PI'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    class Meta:
        model = PrincipalInvestigators
        fields = ['birthdate','age','contact','uid']
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), # default date-format %m/%d/%Y will be used
            
        }
class WebGISExpertForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='WGE'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))

    class Meta:
        model =  WebGISExpert
        fields = ['birthdate','age','contact','uid']
        widgets = {
                    'birthdate': DatePickerInput(format='%Y/%m/%d'), # default date-format %m/%d/%Y will be used
            
        }

class NutritionExpertForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='NE'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model =  NutritionExpert
        fields = ['birthdate','age','contact','uid']
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), # default date-format %m/%d/%Y will be used
            
        }