from django.db import models

# Create your models here.
from django.db import models
from authentication.models import User
# Create your models here.

class Project(models.Model):
    ETAT_ACTIVE ='active' 
    ETAT_SUSPENDED='suspended' 
    ETAT_COMPLETED='completed' 
    ETAT_PAUSED = 'paused'
    STATUS=[ 
        (ETAT_ACTIVE,'active'), 
        (ETAT_SUSPENDED,'suspended'), 
        (ETAT_COMPLETED,'completed'), 
        (ETAT_PAUSED,'paused'), 
    ] 
    name = models.CharField(max_length=255,unique=True)
    description = models.CharField(max_length=500)
    matricule = models.CharField(max_length=255,unique=True)
    status = models.CharField(max_length=50,choices=STATUS,default=ETAT_ACTIVE)
    starter_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="manager",null=True,blank=True)
    assigned_to = models.ManyToManyField(User,related_name="users", blank=True)
    end_date= models.DateField(null=True)