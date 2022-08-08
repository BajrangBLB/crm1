from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Reference_Table (models.Model):
    reference_fileName =  models.CharField(max_length=255, default='') 
    reference_file=  models.FileField(upload_to="") 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self) :
       return str(self.reference_fileName)
      

    def file_url(self):
        return self.myfiles.url



       
class LO_Folder (models.Model):
    f_name = models.CharField(max_length=255, default='')
    myfiles = models.FileField(upload_to="") 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    """ def __str__(self) :
       return str(self.user)
        """

    #this method displays file name for each uploaded file instance
    def __str__(self) :
        return self.f_name

    def file_url(self):
        return self.myfiles.url


class CLO_Folder (models.Model):
    f_name = models.CharField(max_length=255, default='')
    myfiles = models.FileField(upload_to="") 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self) :
       return self.f_name
    
    def file_url(self):
        return self.myfiles.url



