

from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from accounts.decorators import allowed_users

from accounts.xlfunctions import*


from django.core.exceptions import ObjectDoesNotExist




# Create your views here.

from .models import *
from . forms import  CreateUserForm 
 
 



def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
         form = CreateUserForm(request.POST or None)

         if form.is_valid():
             form.save()

             user = form.cleaned_data.get('username')
             
             messages.success(request, 'account was created for '+user)

             return redirect('login')
 

    context = {'form':form}

    return render(request, 'accounts/register.html', context)





def loginPage(request):
    
    

    if request.method =="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username= username, password = password )

        if user is not None:
            login(request ,  user)
            if user.is_superuser:
                return redirect('adminPage')
            else:
                return redirect('landingPage')
        
        else:
            messages.info(request, "Username or password is incorrect")
            
  
    context = {}
    return render(request, 'accounts/login.html', context )

def logoutUser(request):
 logout(request)
 return redirect ('home')
 
 


def home(request):
    return render(request, 'accounts/dashboard.html')


@login_required(login_url='login')
def landingPage(request):
    user = request.user
    files = LO_Folder.objects.filter(user=user)
    files1 = CLO_Folder.objects.filter(user=user)

    print (files)
    context = {        'files' : files  ,'files1' : files1  }


    return render (request , 'accounts/landingPage.html' ,  context)
    


def send_files(request):

    try:
        
        user = request.user
         

     
     
        if request.method == "POST":

           
            course = request.POST.get("course")
            course_code =  request.POST.get("course_code")
            year = request.POST.get("year")
            term = request.POST.get("term")

            
            myfile= request.FILES["fileupload"]
            

            namef=  myfile.name
       
            usernamef= request.user.first_name
            usernamel= request.user.last_name




# file  validations 
            if namef.endswith('.xlsx'):
                #print('yes it is correct excel file')
                if not namef.__contains__('['):
                
   
                    messages.success(request,'Learning Outcomes mapping successfully uploaded')

                    file_name='LO_'+course+'-'+course_code+'_'+term+'_'+year+'_'+usernamel+'_'+usernamef

                    LO_Folder(f_name=file_name,myfiles=myfile , user = user ).save()  
                    context = {}

                    return render (request , 'accounts/landingPage.html' ,  context)

                else:
                    messages.success(request,'LO File is NOT uploaded. Please upload the LO file with correct contents.')

                context = {
                                 
                            }
                
                return render (request , 'accounts/landingPage.html',  context)

            
             
            else :
                #print("the .xls is not correct")
                messages.success(request,'LO File is NOT uploaded. Please upload only excel files with .xlsx extension')

                context = {
                                 
                            }
                
                return render (request , 'accounts/landingPage.html',  context)

    except :
         messages.success(request,'Error occured , please enter the file ')     
         return render (request , 'accounts/landingPage.html')


    '''
def delete(request):
    if request.method == "POST":
        #delete = request.POST.get('delete') 
        file = myuploadfile.object.get(pk=delete)
        file.delete()
    return render (request , 'accounts/landingPage.html')
    ''' 



def send_files2(request):


    try:
        user = request.user
         

        if request.method == "POST":

           
            course = request.POST.get("course")
            year = request.POST.get("year")
            term = request.POST.get("term")

            
            myfile= request.FILES["fileupload2"]
            

            namef=  myfile.name
       
            usernamef= request.user.first_name
            usernamel= request.user.last_name




# file  validations 
            if namef.endswith('.xlsx'):
                if not namef.__contains__('['):
                
                    print('yes it is correct excel file')
    
                    messages.success(request,'Student Marks successfully uploaded')

                    file_name='CLO_'+'Data_'+course+'_'+term+'_'+year+'_'+usernamel+'_'+usernamef

                    CLO_Folder(f_name=file_name,myfiles=myfile , user = user ).save()

                    
                    context = {
                            
                            }

                    return render (request , 'accounts/landingPage.html' ,  context)

            
                else:
                    messages.success(request,'CLO File is NOT uploaded. Please upload the CLO file with correct contents.')
                    context = {
                                 
                            }
                 
                    return render (request , 'accounts/landingPage.html',  context)

            else :
                print("the .xls is not correct")
                messages.success(request,'CLO File is NOT uploaded. Please upload only excel files with .xlsx extension')

                context = {
                                 
                            }
                
                return render (request , 'accounts/landingPage.html',  context)

    except :
         messages.success(request,'Error occured , please enter the file ')     
         return render (request , 'accounts/landingPage.html')





@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def adminPage(request):
    if request.method == "POST":

        GA = request.POST.get('GA_name')
         
        context = {'a':"GA-", 'ga':GA , 'hi':"Aggregated File ready to download"}
        
        """for GA_LIST in GA10:
            print(GA_LIST)
            for course in GA_LIST:
                print (course)"""
                
        if GA == "1":

            try:
                for course in LOa:put_course(1,course,"1a")

                for course in LOb:put_course(1,course,"1b")
                
                for course in LOc:put_course(1,course,"1c")
                
                for course in LOd:put_course(1,course,"1d")
                
                for course in LOe:put_course(1,course,"1e")

                for course in LOf:put_course(1,course,"1f")

            except ObjectDoesNotExist:
                messages.error(request,'WARNING: All required file are not uploaded.')
                messages.error(request,'Please check the empty entries in the Aggregated sheet and upload the missing files.')
            except :
                messages.success(request,'WARNING: ERROR occured.')
                messages.error(request,'Please check the contents of the relevant CLO and LO files.')
                

        if GA == "2":

            try:
                for course in LOa_2:put_course(2,course,"2a")
                for course in LOb_2:put_course(2,course,"2b") 
                for course in LOc_2:put_course(2,course,"2c")
                for course in LOd_2:put_course(2,course,"2d")
                for course in LOe_2:put_course(2,course,"2e")
                for course in LOf_2:put_course(2,course,"2f")
                for course in LOg_2:put_course(2,course,"2g")

            except ObjectDoesNotExist:
                messages.error(request,'WARNING: All required file are not uploaded.')
                messages.error(request,'Please check the empty entries in the Aggregated sheet and upload the missing files.')
            except :
                messages.success(request,'WARNING: ERROR occured.')
                messages.error(request,'Please check the contents of the relevant CLO and LO files.')

        
        if GA == "3":

            try:
                for course in LOa_3:put_course(3,course,"3a")
                for course in LOb_3:put_course(3,course,"3b") 
                for course in LOc_3:put_course(3,course,"3c")
                for course in LOd_3:put_course(3,course,"3d")
                for course in LOe_3:put_course(3,course,"3e")
                for course in LOf_3:put_course(3,course,"3f")
                

            except ObjectDoesNotExist:
                messages.error(request,'WARNING: All required file are not uploaded.')
                messages.error(request,'Please check the empty entries in the Aggregated sheet and upload the missing files.')
            except :
                messages.success(request,'WARNING: ERROR occured.')
                messages.error(request,'Please check the contents of the relevant CLO and LO files.')
        if GA == "4":

            try:
                for course in LOa_4:put_course(4,course,"4a")
                for course in LOb_4:put_course(4,course,"4b") 
                for course in LOc_4:put_course(4,course,"4c")
                for course in LOd_4:put_course(4,course,"4d")
                for course in LOe_4:put_course(4,course,"4e")
                for course in LOf_4:put_course(4,course,"4f")
                for course in LOg_4:put_course(4,course,"4g")
                for course in LOh_4:put_course(4,course,"4h")

            except ObjectDoesNotExist:
                messages.error(request,'WARNING: All required file are not uploaded.')
                messages.error(request,'Please check the empty entries in the Aggregated sheet and upload the missing files.')
            except :
                messages.success(request,'WARNING: ERROR occured.')
                messages.error(request,'Please check the contents of the relevant CLO and LO files.')

        if GA == "5":

            try:
                for course in LOa_5:put_course(5,course,"5a")
                for course in LOb_5:put_course(5,course,"5b") 
                for course in LOc_5:put_course(5,course,"5c")
                for course in LOd_5:put_course(5,course,"5d")
                for course in LOe_5:put_course(5,course,"5e")
                
            except ObjectDoesNotExist:
                messages.error(request,'WARNING: All required file are not uploaded.')
                messages.error(request,'Please check the empty entries in the Aggregated sheet and upload the missing files.')
            except :
                messages.success(request,'WARNING: ERROR occured.')
                messages.error(request,'Please check the contents of the relevant CLO and LO files.')

        if GA == "6":

            try:
                for course in LOa_6:put_course(6,course,"6a")
                for course in LOb_6:put_course(6,course,"6b") 
                for course in LOc_6:put_course(6,course,"6c")
                for course in LOd_6:put_course(6,course,"6d")
                for course in LOe_6:put_course(6,course,"6e")
                for course in LOf_6:put_course(6,course,"6f")
             

            except ObjectDoesNotExist:
                messages.error(request,'WARNING: All required file are not uploaded.')
                messages.error(request,'Please check the empty entries in the Aggregated sheet and upload the missing files.')
            except :
                messages.success(request,'WARNING: ERROR occured.')
                messages.error(request,'Please check the contents of the relevant CLO and LO files.')

        if GA == "7":

            try:
                for course in LOa_7:put_course(7,course,"7a")
                for course in LOb_7:put_course(7,course,"7b") 
                for course in LOc_7:put_course(7,course,"7c")
                for course in LOd_7:put_course(7,course,"7d")
                for course in LOe_7:put_course(7,course,"7e")
                for course in LOf_7:put_course(7,course,"7f")
                for course in LOg_7:put_course(7,course,"7g")
                for course in LOh_7:put_course(7,course,"7h")
             

            except ObjectDoesNotExist:
                messages.error(request,'WARNING: All required file are not uploaded.')
                messages.error(request,'Please check the empty entries in the Aggregated sheet and upload the missing files.')
            except :
                messages.success(request,'WARNING: ERROR occured.')
                messages.error(request,'Please check the contents of the relevant CLO and LO files.')

        if GA == "8":

            try:
                for course in LOa_8:put_course(8,course,"8a")
                for course in LOb_8:put_course(8,course,"8b") 
                for course in LOc_8:put_course(8,course,"8c")
                for course in LOd_8:put_course(8,course,"8d")
                for course in LOe_8:put_course(8,course,"8e")
                for course in LOf_8:put_course(8,course,"8f")
             

            except ObjectDoesNotExist:
                messages.error(request,'WARNING: All required file are not uploaded.')
                messages.error(request,'Please check the empty entries in the Aggregated sheet and upload the missing files.')
            except :
                messages.success(request,'WARNING: ERROR occured.')
                messages.error(request,'Please check the contents of the relevant CLO and LO files.')

        if GA == "9":

            try:
                for course in LOa_9:put_course(9,course,"9a")
                for course in LOb_9:put_course(9,course,"9b") 
                for course in LOc_9:put_course(9,course,"9c")
                for course in LOd_9:put_course(9,course,"9d")
                for course in LOe_9:put_course(9,course,"9e")
                for course in LOf_9:put_course(9,course,"9f")
                for course in LOg_9:put_course(9,course,"9g")
              

            except ObjectDoesNotExist:
                messages.error(request,'WARNING: All required file are not uploaded.')
                messages.error(request,'Please check the empty entries in the Aggregated sheet and upload the missing files.')
            except :
                messages.success(request,'WARNING: ERROR occured.')
                messages.error(request,'Please check the contents of the relevant CLO and LO files.')

        if GA == "10":

            try:
                for course in LOa_10:put_course(10,course,"10a")

                for course in LOb_10:put_course(10,course,"10b")
                
                for course in LOc_10:put_course(10,course,"10c")
                
                for course in LOd_10:put_course(10,course,"10d")
                
                for course in LOe_10:put_course(10,course,"10e")

                for course in LOf_10:put_course(10,course,"10f")

            except ObjectDoesNotExist:
                messages.error(request,'WARNING: All required file are not uploaded.')
                messages.error(request,'Please check the empty entries in the Aggregated sheet and upload the missing files.')
            except :
                messages.success(request,'WARNING: ERROR occured.')
                messages.error(request,'Please check the contents of the relevant CLO and LO files.')

        if GA == "11":

            try:
                for course in LOa_11:put_course(11,course,"11a")
                for course in LOb_11:put_course(11,course,"11b") 
                for course in LOc_11:put_course(11,course,"11c")
                for course in LOd_11:put_course(11,course,"11d")
                for course in LOe_11:put_course(11,course,"11e")
                for course in LOf_11:put_course(11,course,"11f")
               

            except ObjectDoesNotExist:
                messages.error(request,'WARNING: All required file are not uploaded.')
                messages.error(request,'Please check the empty entries in the Aggregated sheet and upload the missing files.')
            except :
                messages.success(request,'WARNING: ERROR occured.')
                messages.error(request,'Please check the contents of the relevant CLO and LO files.')
        if GA == "12":

            try:
                for course in LOa_12:put_course(12,course,"12a")
                for course in LOb_12:put_course(12,course,"12b") 
                for course in LOc_12:put_course(12,course,"12c")
                for course in LOd_12:put_course(12,course,"12d")
                for course in LOe_12:put_course(12,course,"12e")
                for course in LOf_12:put_course(12,course,"12f")
               

            except ObjectDoesNotExist:
                messages.error(request,'WARNING: All required file are not uploaded.')
                messages.error(request,'Please check the empty entries in the Aggregated sheet and upload the missing files.')
            except :
                messages.success(request,'WARNING: ERROR occured.')
                messages.error(request,'Please check the contents of the relevant CLO and LO files.')


        return render (request , 'accounts/adminPage.html',context)
     

    
    return render (request , 'accounts/adminPage.html',)
 

  