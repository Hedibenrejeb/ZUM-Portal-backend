import os
from rest_framework.generics import *
from rest_framework import status ,permissions
from rest_framework import generics,status,views
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from .models import User
from django.core.mail import EmailMultiAlternatives

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import smart_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated

class updateDestroyUserApiView(RetrieveUpdateDestroyAPIView):
    # authentication_classes = []
    queryset=User.objects.all()
    serializer_class = userSerializer
    lookup_field="id"
    def get_queryset(self):
        return self.queryset

class GetAllUser(ListAPIView):
    authentication_classes = []
    serializer_class = userSerializer
    queryset = User.objects.all()
    def get_queryset(self):
        return self.queryset.all()

class GetAllUsers(ListAPIView):
    authentication_classes = []
    pagination_class = None
    serializer_class = userSerializer
    queryset = User.objects.all()
    def get_queryset(self):
        return self.queryset.all()

class UpdateAfterRegister(UpdateAPIView):
    authentication_classes = []
    serializer_class = Registerserilaizer
    lookup_field = "id"
    queryset = User.objects.all()

class RegisterUserViaEmail(GenericAPIView):
    authentication_classes = []
    serializer_class = RegisterUserSerializer
    def post(self, request):
        user = request.data
        serilaizer = self.serializer_class(data=user)
        serilaizer.is_valid(raise_exception=True)
        serilaizer.save()
        user_data = serilaizer.data
        print(user_data)
        user = User.objects.get(id=user_data['id'])
        # current_site = get_current_site(request).domain
        # relativelink = reverse('UpdateAfterRegister', kwargs={'id': user_data['id']})
        # absurl = 'http://'+current_site + relativelink
        absurl = 'http://localhost:4200/account/auth/signup/'+str(user_data['id'])
        email_body = "<html><head><meta http-equiv='Content-Type' content='text/html; charset=utf-8' /></head><body><div class=''><div style='background:#f9f9f9'><div style='margin:0px auto;max-width:640px;background:transparent'><table role='presentation' cellpadding='0' cellspacing='0'style='font-size:0px;width:100%;background:transparent' align='center' border='0'><tbody><tr><td style='text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:40px 0px'><div aria-labelledby='mj-column-per-100' class='m_4819380286727024960mj-column-per-100'style='vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%'><table role='presentation' cellpadding='0' cellspacing='0' width='100%'border='0'><tbody><tr><td style='word-break:break-word;font-size:0px;padding:0px'align='center'><table role='presentation' cellpadding='0' cellspacing='0'style='border-collapse:collapse;border-spacing:0px'align='center' border='0'><tbody><tr><td style='width:138px'></td></tr></tbody></table></td></tr></tbody></table></div></td></tr></tbody></table></div><div style='max-width:640px;margin:0 auto;border-radius:4px;overflow:hidden'><div style='margin:0px auto;max-width:640px;background:#ffffff'><table role='presentation' cellpadding='0' cellspacing='0'style='font-size:0px;width:100%;background:#ffffff' align='center' border='0'><tbody><tr><td style='text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:40px 50px'><table role='presentation' cellpadding='0' cellspacing='0' width='100%' border='0'><tbody><tr><td style='word-break:break-word;font-size:0px;padding:0px'><div style='color:#737f8d;font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-size:16px;line-height:24px;text-align:left'><h2 style='font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-weight:500;font-size:20px;color:#4f545c;letter-spacing:0.27px'align='center'><b>Welcome to ZUM PORTAL</b></h2></div></td></tr><tr><td style='word-break:break-word;font-size:0px;padding:30px 0px'><p style='font-size:1px;margin:0px auto;border-top:1px solid #dcddde;width:100%'></p></td></tr><tr><td style='word-break:break-word;font-size:0px;padding:0px'><div style='color:#737f8d;font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-size:16px;line-height:24px;text-align:left' ><p align='center'>Click on this button to complete your registration</p></div></td></tr><tr><td style='word-break:break-word;font-size:0px;padding:10px 25px;padding-top:20px'align='center'><table role='presentation' cellpadding='0' cellspacing='0' style='border-collapse:separate'align='center' border='0'><tbody><tr><td style='border:none;border-radius:3px;color:white;padding:15px 19px' align='center' valign='middle'><form action="+absurl+"><input value='Register'type='submit' align='center' style='padding:12px 24px;color:#ffffff;font-weight:400;display:inline-block;text-decoration:none;font-size:16px;line-height:1.25em;border-color:#0a66c2;background-color:#4b71ed;border-radius:34px;border-width:1px;border-style:solid'></form></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></div></div><div style='margin:0px auto;max-width:640px;background:transparent'><table role='presentation' cellpadding='0' cellspacing='0' style='font-size:0px;width:100%;background:transparent' align='center' border='0'><tbody><tr><td style='text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:20px 0px'><div aria-labelledby='mj-column-per-100' class='m_4819380286727024960mj-column-per-100' style='vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%'><table role='presentation' cellpadding='0' cellspacing='0' width='100%' border='0'><tbody><tr><td style='word-break:break-word;font-size:0px;padding:0px'align='center' ><div style='color:#99aab5;font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-size:12px;line-height:24px;text-align:center'><strong>Copyright &copy; ZUM-IT</strong><br>Sent with &#10084; from ZUM-PORTAL.</div></td></tr></tbody></table></div></td></tr></tbody></table></div></div></div></body></html>"
        data = {'email_body': email_body, 'email_to': user.email,'email_subject': 'Continue your registration'}
        email = EmailMultiAlternatives(subject = data['email_subject'], body = 'email_body', to =[data['email_to']])
        email.attach_alternative(email_body, "text/html")
        email.send()
        return Response(user_data, status = status.HTTP_201_CREATED)

class LoginAPIView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    def post(self,request):
        serializer= self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class AuthUserAPIView(generics.GenericAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    def get(self,request):
        user=User.objects.get(pk=request.user.pk)
        serializer=userSerializer(user)
        return Response(serializer.data)       

class LogoutAPIView(generics.GenericAPIView):
    serializer_class=LogoutSerializer
    permission_classes=(permissions.IsAuthenticated,)
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    # permission_classes = (IsAuthenticated,)
    def get_object(self, queryset=None):
        obj = User.objects.get(id =self.kwargs['id'])
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# import socket
# socket.getaddrinfo('localhost', 8080)
class PasswordRestEmail(generics.GenericAPIView):
    authentication_classes = []
    serializer_class = ResetPPasswordEmailSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data['email']
        if User.objects.values().filter(email= email):
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            # current_site = get_current_site(request=request).domain
            # relativelink = reverse('password-reset-complete')
            # absurl = 'http://'+current_site +relativelink
            absurl = 'http://localhost:4200/account/updatepassword'+";token="+str(token)+";u="+uidb64
            email_body = "<html><head><meta http-equiv='Content-Type' content='text/html; charset=utf-8' /></head><body><div class=''><div style='background:#f9f9f9'><div style='margin:0px auto;max-width:640px;background:transparent'><table role='presentation' cellpadding='0' cellspacing='0'style='font-size:0px;width:100%;background:transparent' align='center' border='0'><tbody><tr><td style='text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:40px 0px'><div aria-labelledby='mj-column-per-100' class='m_4819380286727024960mj-column-per-100'style='vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%'><table role='presentation' cellpadding='0' cellspacing='0' width='100%'border='0'><tbody><tr><td style='word-break:break-word;font-size:0px;padding:0px'align='center'><table role='presentation' cellpadding='0' cellspacing='0'style='border-collapse:collapse;border-spacing:0px'align='center' border='0'><tbody><tr><td style='width:138px'></td></tr></tbody></table></td></tr></tbody></table></div></td></tr></tbody></table></div><div style='max-width:640px;margin:0 auto;border-radius:4px;overflow:hidden'><div style='margin:0px auto;max-width:640px;background:#ffffff'><table role='presentation' cellpadding='0' cellspacing='0'style='font-size:0px;width:100%;background:#ffffff' align='center' border='0'><tbody><tr><td style='text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:40px 50px'><table role='presentation' cellpadding='0' cellspacing='0' width='100%' border='0'><tbody><tr><td style='word-break:break-word;font-size:0px;padding:0px'><div style='color:#737f8d;font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-size:16px;line-height:24px;text-align:left'><h2 style='font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-weight:500;font-size:20px;color:#4f545c;letter-spacing:0.27px'align='center'><b>Welcome to ZUM PORTAL</b></h2></div></td></tr><tr><td style='word-break:break-word;font-size:0px;padding:30px 0px'><p style='font-size:1px;margin:0px auto;border-top:1px solid #dcddde;width:100%'></p></td></tr><tr><td style='word-break:break-word;font-size:0px;padding:0px'><div style='color:#737f8d;font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-size:16px;line-height:24px;text-align:left' ><p align='center'>Click on this button to change your password</p></div></td></tr><tr><td style='word-break:break-word;font-size:0px;padding:10px 25px;padding-top:20px'align='center'><table role='presentation' cellpadding='0' cellspacing='0' style='border-collapse:separate'align='center' border='0'><tbody><tr><td style='border:none;border-radius:3px;color:white;padding:15px 19px' align='center' valign='middle'><form action="+absurl+"><input value='Reset password'type='submit' align='center' style='padding:12px 24px;color:#ffffff;font-weight:400;display:inline-block;text-decoration:none;font-size:16px;line-height:1.25em;border-color:#0a66c2;background-color:#4b71ed;border-radius:34px;border-width:1px;border-style:solid'></form></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></div></div><div style='margin:0px auto;max-width:640px;background:transparent'><table role='presentation' cellpadding='0' cellspacing='0' style='font-size:0px;width:100%;background:transparent' align='center' border='0'><tbody><tr><td style='text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:20px 0px'><div aria-labelledby='mj-column-per-100' class='m_4819380286727024960mj-column-per-100' style='vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%'><table role='presentation' cellpadding='0' cellspacing='0' width='100%' border='0'><tbody><tr><td style='word-break:break-word;font-size:0px;padding:0px'align='center' ><div style='color:#99aab5;font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-size:12px;line-height:24px;text-align:center'><strong>Copyright &copy; ZUM-IT</strong><br>Sent with &#10084; from ZUM-PORTAL.</div></td></tr></tbody></table></div></td></tr></tbody></table></div></div></div></body></html>"
            data = {'email_body': email_body, 'email_to': user.email,'email_subject': 'Reset your password'}
            email = EmailMultiAlternatives(subject = data['email_subject'], body = 'email_body', to =[data['email_to']])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response({'success':'We have sent you a link to reset your password','uidb64': uidb64, 'token': token},status=status.HTTP_200_OK)
        return Response({'error': 'User does not exist'},status=status.HTTP_404_NOT_FOUND)

class SetNewPasswordApiView(generics.GenericAPIView):
    authentication_classes = []
    serializer_class = SetNewPasswordSerialize
    def patch(self,request):
        serilaizer = self.serializer_class(data=request.data)
        serilaizer.is_valid(raise_exception=True)
        return Response({'success':True,'message':'Password resert success'},status=status.HTTP_200_OK)