from django.contrib.auth.models import User
from rest_framework import serializers
import uuid
import re 



class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField( default=uuid.uuid4)  
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    date_joined= serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['user_id','username','password','email','date_joined','confirm_password']

    def validate_password(self,value):
        if not re.search(r'[A-Z]',value):
            raise serializers.ValidationError('password must contain one upper letter')
        
        if not re.search(r'\d',value):
            raise serializers.ValidationError('password must contain at least one number')

        if len(value)<=6:
            raise serializers.ValidationError('password must be atleast 6 characters')
        return value


    def validate(self,data):
        # validate both passwords
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({'error':'passwords do not match'})
        if User.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError({'error':'username already exists'})
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')  # We don’t need to save this
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])  # Hash password
        user.save()
        return user