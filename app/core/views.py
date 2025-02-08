from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ProjectSerializer,SkillSerializer
from .models import Project,Skill
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

class ProjectView(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def get(self,request):
        model = Project.objects.all()
        serializer = ProjectSerializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        try:
            instance = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
        serializer = ProjectSerializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        try:
            instance = Project.objects.get(pk=pk)
            instance.delete()
            return Response({'message':'deleted'},status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        


class SkillView(APIView):
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]

    def get(self,request):
        model = Skill.objects.all()
        serializer = SkillSerializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        try:
            instance = Skill.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
        serializer = SkillSerializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        try:
            instance = Skill.objects.get(pk=pk)
            instance.delete()
            return Response({'message':'deleted'},status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ExperienceAdmin(CreateAPIView,RetrieveUpdateDestroyAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [IsAdminUser]
    queryset = Experience.objects.all()

class ExperienceView (ListAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [AllowAny]   
    queryset = Experience.objects.all()

class EducationAdmin(CreateAPIView,RetrieveUpdateDestroyAPIView):
    serializer_class = EducationSerializer
    permission_classes = [IsAdminUser]
    queryset = Education.objects.all()    

class EducationView(ListAPIView):
    serializer_class = EducationSerializer
    permission_classes = [AllowAny]
    queryset = Education.objects.all()       