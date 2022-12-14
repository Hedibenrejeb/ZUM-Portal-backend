from datetime import datetime, timezone
from django.shortcuts import render
from rest_framework.generics import GenericAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
import authentication
from authentication.models import User
from task.models import Task
from task.permissions import IsOwner
from rest_framework import permissions

from task.serializers import GetTasksUsers, Taskserilaizer,TaskOwnerSerializer,UpdateTaskserilaizer,TaskAffectedToSerializer,TaskProjectSerializer,TaskOwnerSerializer
from rest_framework import status,response
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.
class CreateTaskApiView(GenericAPIView):
    authentication_classes = []
    serializer_class = Taskserilaizer
    def post(self,request):
        serilaizer = self.serializer_class(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return response.Response(serilaizer.data,status=status.HTTP_201_CREATED)
        return response.Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)


class getTaskApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    queryset=Task.objects.all()
    serializer_class = GetTasksUsers
    lookup_field="id"
    def get_queryset(self):
        return self.queryset



class updateDestroyTaskApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    queryset=Task.objects.all()
    serializer_class = UpdateTaskserilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset

class DestroyTaskApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    queryset=Task.objects.all()
    #  serializer_class = UpdateTaskserilaizer

    lookup_field="id"
    def get_queryset(self):
        return self.queryset



class GetTaskUsersApiView(GenericAPIView):
    authentication_classes = []
    serializer_class=GetTasksUsers
    queryset = Task.objects.all()

    def get(self,request):
        queryset = self.get_queryset()
        serializer = GetTasksUsers(queryset, many=True)
        return response.Response(serializer.data)



class GetTaskByUser(ListAPIView):
    authentication_classes=[]
    serializer_class = TaskAffectedToSerializer
    pagination_class = None

    def get_queryset(self):
        return Task.objects.values().filter(affectedTo = self.kwargs['id'])



class GetTaskByCreator(ListAPIView):
    authentication_classes=[]
    serializer_class = TaskOwnerSerializer
    pagination_class = None

    def get_queryset(self):
        return Task.objects.values().filter(creator = self.kwargs['id'])

class GetTaskByProject(ListAPIView):
    authentication_classes=[]
    serializer_class = TaskProjectSerializer
    pagination_class = None
    def get_queryset(self):
        
        return Task.objects.values().filter(project = self.kwargs['id'])
              


#  get task by creator (with access token)
class TaskListcreatorAPIView(ListAPIView):
    # authentication_classes = [authentication,]
    permission_classes=(permissions.IsAuthenticated,)
    serializer_class=TaskOwnerSerializer 
    lookup_field="id"
    pagination_class = None

    queryset= Task.objects.all()
    # def get_queryset(self):
    #     return self.queryset.filter(creator=self.request.user)  
    def get_queryset(self):
      return super().get_queryset().filter(creator__id=self.request.user.id)     

""" class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(permissions.IsAuthenticated,IsOwner,)
    serializer_class=ExpenseSerializer 

    queryset= Expense.objects.all()
    lookup_field="id"
    # def perform_create(self, serializer):return serializer.save(owner=self.request.user) 
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)  """       
