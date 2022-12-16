from rest_framework import serializers
from authentication.models import User 
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from .models import User
from django.utils.encoding import smart_str,force_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import password_validation
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','role']

class Registerserilaizer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=120,min_length=6,write_only=True)
    class Meta:
        model = User
        fields = ('firstname','lastname','password','id',)
    def update(self, instance, validated_data):
        instance.firstname = validated_data.pop('firstname', instance.firstname)
        instance.lastname = validated_data.pop('lastname', instance.lastname)
        instance.set_password(validated_data.pop('password'))
        instance.save()
        return instance

class UserAssginedToProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email',)

class userSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields =('id','firstname','email', 'lastname','role',)  

class LoginSerializer(serializers.ModelSerializer): 
    email=serializers.EmailField(max_length=255,min_length=3)
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    firstname=serializers.CharField(max_length=68,min_length=6,read_only=True)
    lastname=serializers.CharField(max_length=68,min_length=6,read_only=True)
    role=serializers.CharField(max_length=68,min_length=6,read_only=True)
    tokens=serializers.SerializerMethodField()

    def get_tokens(self,obj):
        # 1/ get the real user from obj
        user =User.objects.get(email=obj['email'])
        return{
            'token' :user.tokens(),
          #  'access':user.tokens()['access'],
          #  'refresh':user.tokens()['refresh'], 
        }
    class Meta: 
        model =User 
        fields=['id','firstname','lastname','email','role','password','tokens','token',]
        read_only_fields =['token']
    
    def validate(self,attrs):
        email=attrs.get('email','')
        password=attrs.get('password','')
        user=auth.authenticate(email=email,password=password)
        if not user :
            raise AuthenticationFailed('Invalid credentials, try again ')
        """  if not user.is_active :
            raise AuthenticationFailed('Account disabled , contact admin ')
        if not user.is_verified :
            raise AuthenticationFailed('Email is not verified ')    
         """
        return{
            'id':user.id,
            'role':user.role,
            'email': user.email,
            'lastname': user.lastname,
            'firstname': user.firstname,
            'tokens': user.tokens(),
            'token' :user.token
        }
        return super().validate(attrs)

class LogoutSerializer(serializers.Serializer): 
    refresh=serializers.CharField()
    default_error_messages ={
        'bad_token':('Token is expired or invalid')
    }
    def validate(self, attrs):
       self.token=attrs['refresh']
       return attrs

    def save(self,**kwargs):
        try:
         RefreshToken(self.token).blacklist()
        except TokenError :
            self.fail('bad_token')

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)
    class Meta:
        fields = ['email']

class SetNewPasswordSerialize(serializers.Serializer):
    password = serializers.CharField(min_length=6,max_length=68,write_only=True)
    token = serializers.CharField(min_length=1,write_only=True)
    uidb64 = serializers.CharField(min_length=1,write_only=True)
    class Meta:
        fields = ['password','token','uidb64']
    def validate(self, attrs):
        try:
          password = attrs.get('password')
          token = attrs.get('token')    
          uidb64 = attrs.get('uidb64')  
          id=force_str(urlsafe_base64_decode(uidb64))
          user = User.objects.get(id=id)
          if not PasswordResetTokenGenerator().check_token(user,token):
            raise AuthenticationFailed('The reset link is invalide',401)
          user.set_password(password)
          user.save()
          return user
        except Exception as exp:
            raise AuthenticationFailed('The reset link is invalide',401)
        return super().validate(attrs)
