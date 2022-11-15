from django.urls import path
from authentication import views
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns=[
    path('login/',views.LoginAPIView.as_view(),name="login"),
    path('logout/',views.LogoutAPIView.as_view(),name="logout"),
    path('user/',views.AuthUserAPIView.as_view(),name="auth-user"),
    path('listuser/',views.GetAllUsers.as_view(),name="list-user"),
    path('list-user/', views.GetAllUser.as_view(), name='list-user'),
    path('register-user/',views.RegisterUserViaEmail.as_view(),name='register-user'),
    path('updateafterregister/<str:id>', views.UpdateAfterRegister.as_view(), name='UpdateAfterRegister'),
    path('updateUser/<int:id>',views.updateDestroyUserApiView.as_view(),name='updateuser'),
    path('deleteUser/<int:id>',views.updateDestroyUserApiView.as_view(),name='deleteuser'),
]