# from email.policy import default
# from typing_extensions import Required
from django.db import models 
from django.contrib.auth.models import(AbstractBaseUser,BaseUserManager,) 
from rest_framework_simplejwt.tokens import RefreshToken 
import jwt 
from django.conf import settings
from datetime import datetime,timedelta
from django.contrib.auth.models import(AbstractBaseUser,BaseUserManager,AbstractUser,PermissionsMixin)

# Create your models here. 

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
    role=models.CharField(max_length=2,choices=ROLES_CHOICES,default=SIMPLE_USER) 
    email=models.EmailField(max_length=255,unique=True)
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

    @property
    def token(self):
        token=jwt.encode(
        {'firstname':self.firstname,'email':self.email,
            'exp':datetime.utcnow()+timedelta(hours=24)},
                settings.SECRET_KEY,algorithm='HS256')
        return token