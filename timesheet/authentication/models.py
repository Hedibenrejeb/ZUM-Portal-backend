# from email.policy import default
# from typing_extensions import Required
from django.db import models 
from django.contrib.auth.models import(AbstractBaseUser,BaseUserManager,) 
from rest_framework_simplejwt.tokens import RefreshToken 
import jwt 
from django.conf import settings
from datetime import datetime,timedelta
from django.contrib.auth.models import(AbstractBaseUser,BaseUserManager,AbstractUser,PermissionsMixin)
from PIL import Image
from django.utils.translation import gettext_lazy as _

# Create your models here. 

def upload_to(instance, filename):

    return 'users/{filename}'.format(filename=filename)


class UserManager(BaseUserManager): 
    def create_user(self,email,role,password=None): 
      
       if email is None : 
            raise TypeError('Users should have a email')
       user =self.model(role=role,email=self.normalize_email(email)) 
    #    user =self.model(firstname=firstname,lastname=lastname,email=self.normalize_email(email)) 
       user.set_password(password)  
       user.save() 
       return user  

    def create_superuser(self,email,password=None): 
       if password is None: 
        raise TypeError('Password should not be None') 
       user=self.create_user(email,password)   
       user.save()  
       return user 

def upload_path(instance, filname):
    return '/'.join(['images', str(instance.firstname), filname])

class User(AbstractBaseUser,PermissionsMixin): 
    MANAGER ='MG' 
    SIMPLE_USER='SU' 
    ADMIN='AD' 
    ROLES_CHOICES=[ 
        (MANAGER,'manager'), 
        (SIMPLE_USER,'simple_user'), 
        (ADMIN,'admin'), 
    ] 
    firstname=models.CharField(max_length=255,null=True)  
    lastname=models.CharField(max_length=255,null=True)  
    Mobile=models.CharField(max_length=255,null=True) 
    Location=models.CharField(max_length=255,null=True) 
    Experience=models.CharField(max_length=255,null=True)  
    role=models.CharField(max_length=2,choices=ROLES_CHOICES,default=SIMPLE_USER) 
    email=models.EmailField(max_length=255,unique=True)
    #photo = models.ImageField(upload_to=upload_path,blank=True, null=True,max_length=255)
    photo = models.ImageField(_('photo'),upload_to=upload_to,default='users/default.png')
    USERNAME_FIELD ='email'  
    REQUIRED_FIELDS =['role',] 
    objects = UserManager() 
    def __str__(self): 
        return self.email 
    def tokens(self): 
        refresh=RefreshToken.for_user(self) 
        return {
            'refresh':str(refresh),  
            'access':str(refresh.access_token) 
        }
    def save(self, *args, **kwargs):
         super().save(*args, **kwargs)
         img = Image.open(self.photo.path) # Open image using self
         if img.height > 300 or img.width > 300:
             new_img = (300, 300)
             img.thumbnail(new_img)
             img.save(self.photo.path)  # saving image at the same path

    

    @property
    def token(self):
        token=jwt.encode(
        {'firstname':self.firstname,'email':self.email,
            'exp':datetime.utcnow()+timedelta(hours=24)},
                settings.SECRET_KEY,algorithm='HS256')
        return token

