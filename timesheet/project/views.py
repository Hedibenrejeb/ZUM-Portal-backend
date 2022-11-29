from rest_framework import permissions
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from .models import Project
from .serializers import GetProjectByUserSerilaizer, ProjectSerilaizer,GetProjectSerilaizer,UpdateProjectSerilaizer,GetAllProjectSerilaizer,GetProjectBycreatorSerilaizer,GetProjectBycreatorWithAffectedToSerilaizer
# Create your views here.
class CreateProject(CreateAPIView):
    authentication_classes=[]
    serializer_class = ProjectSerilaizer
    queryset = Project.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        return serializer.save()

class ListProject(ListAPIView):
    authentication_classes=[]
    serializer_class = GetProjectSerilaizer
    queryset = Project.objects.all()
    def get_queryset(self):
        return self.queryset.all()

class updateDestroyProjectApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Project.objects.all()
    serializer_class = UpdateProjectSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset
        # for nesrine
class getProjectApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset=Project.objects.all()
    serializer_class = GetProjectSerilaizer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset



class ListallProject(ListAPIView):
    authentication_classes=[]
    serializer_class = GetAllProjectSerilaizer
    queryset = Project.objects.all()
    def get_queryset(self):
        return self.queryset.all()
        
class GetProjectByUser(ListAPIView):
    authentication_classes=[]
    serializer_class = GetProjectByUserSerilaizer
    def get_queryset(self):
        return Project.objects.values().filter(assigned_to = self.kwargs['id'])

class GetSommeProjectByUser(ListAPIView):
    authentication_classes=[]
    serializer_class = GetProjectByUserSerilaizer
    def get_queryset(self):
        return Project.objects.values().filter(assigned_to = self.kwargs['id']).sum()


class GetProjectByCreator(ListAPIView):
    authentication_classes=[]
    serializer_class = GetProjectBycreatorSerilaizer
    def get_queryset(self):
        return Project.objects.values().filter(created_by = self.kwargs['id'])



class GetProjectByCreatorWithaffectedTo(ListAPIView):
    authentication_classes=[]
    serializer_class = GetProjectBycreatorWithAffectedToSerilaizer
    
    def get_queryset(self):
        q = Project.objects.values().filter(created_by = self.kwargs['id'])
        t=q['assigned_to']      
        return q       