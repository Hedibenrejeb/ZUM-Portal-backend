from django.urls import path
from project import views

urlpatterns = [
    path('add-project/',views.CreateProject.as_view(),name='add-project'),
    path('list-project/',views.ListProject.as_view(),name='list-project'),
    # path('update-project/<int:id>/',views.UpdateProject.as_view(),name='update-project'),
    path('delete-project/<int:id>',views.updateDestroyProjectApiView.as_view(),name='delete-project'),
    path('update-project/<int:id>',views.updateDestroyProjectApiView.as_view(),name='update-project'),
    path('getproject/<int:id>',views.getProjectApiView.as_view(),name='get-project'),
    path('listproject/',views.ListallProject.as_view(),name='listallproject'),
    path('GetProjectByUser/<int:id>',views.GetProjectByUser.as_view(),name='GetProjectByUser'),
    path('GetProjectByCreator/<int:id>',views.GetProjectByCreator.as_view(),name='GetProjectByCreator'),
    # path('GetProjectByCreatorWithaffectedTo/<int:id>',views.GetProjectByCreatorWithaffectedTo.as_view(),name='GetProjectByCreatorWithaffectedTo'),

    
]