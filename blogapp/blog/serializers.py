from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email","password"]
        extra_kwargs = {'password':{'write_only': True}}
        
    def create(self,validated_data):
            instance = self.Meta.model(**validated_data)
            password = validated_data.pop('password',None)
            if password is not None:
                instance.set_password(password)
                instance.save()
                return instance
                
    
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
        
class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'