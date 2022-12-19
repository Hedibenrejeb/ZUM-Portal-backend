from dataclasses import fields
from rest_framework import serializers
from authentication.models import User 
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from .models import User

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
    # photo = serializers.ImageField(required=False)
    class Meta:
        model = User
        fields =('id','firstname','email','lastname','Location','Mobile','Experience','role','photo')

class UserProfileSerializer(serializers.ModelSerializer): 
    # photo = serializers.ImageField(required=True)
    class Meta:
        model = User
        fields =('id','firstname','email','lastname','Location','Mobile','Experience','photo')  

class ProfileAvatarSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    class Meta:
        model=User
        fields=('photo',)
    def update(self,instance,validated_data):
        print("0000001",validated_data)
        instance.photo=validated_data.pop('photo',instance.photo)
        instance.save()
        return instance

class ProfileSerializer(serializers.ModelSerializer): 
    photo = serializers.ImageField(required=False)
    class Meta:
        model = User
        fields =('id','firstname','email', 'lastname','Location','Mobile','Experience','role','photo')


class LoginSerializer(serializers.ModelSerializer): 
    email=serializers.EmailField(max_length=255,min_length=3)
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    firstname=serializers.CharField(max_length=68,min_length=6,read_only=True)
    lastname=serializers.CharField(max_length=68,min_length=6,read_only=True)
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
        fields=['id','firstname','lastname','email','role','password','tokens','token','photo']
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
            'token' :user.token,
            'photo':user.photo,
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

class UserPhotoSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    class Meta:
        model = User
        fields =('id','photo',)



# class testPhotoSerializer(serializers.ModelSerializer):
#     photo = serializers.ImageField(required=False)
#     class Meta:
#         model = User
#         fields =('photo',)        