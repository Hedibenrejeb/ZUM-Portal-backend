# from django.db import models
from datetime import date, datetime
from email.policy import default
from typing_extensions import Required
from djongo import models 
from authentication.models import User
from authentication.serializers import userSerializer
import json

from project.models import Project 
class Task(models.Model):
    
#    
    STATUS_OPTIONS=[
        ('COMPLETED','COMPLETED'),
        ('INPROGRESS','INPROGRESS'),
        ('UNSTARTED','UNSTARTED'),
        ('CANCEL','CANCEL'),
    ]
    status=models.CharField(choices=STATUS_OPTIONS,max_length=255)
    description=models.TextField()
    name=models.TextField(default="")
    creator=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='creator',default=3)
    enddate= models.DateField(null=False,blank=False)
    updatedate= models.DateField(null=False,blank=False)
    createdate= models.DateField(null=False,blank=False)
    startdate=models.DateField(null=False,blank=False)
    affectedTo=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='affectedTo',default=3)
    project=models.ForeignKey(to=Project,on_delete=models.CASCADE,related_name='project',default=3)



