from rest_framework import serializers
from .models import User,Education,Experience,Skill,Project
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','password']
        extra_kwargs = {
            'password':{'write_only':True},
        }

        def create(self,validated_data):
            validated_data['password'] = make_password(validated_data['password'])
            return super().create(validated_data)
        
        def update(self, instance, validated_data):
            if 'password' in validated_data:
                instance.password = make_password(validated_data['password'])
                validated_data.pop('password')
            return super().update(instance, validated_data)
        

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'        


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__' 

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'          

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'                                     