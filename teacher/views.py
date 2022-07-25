from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from teacher.serializer import TeacherSerializer
from . import serializer
from .models import Teacher


@api_view(['POST'])
def createTeacher(request):
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(

        )
    return Response(serializer.data)


@api_view(['GET'])
def getTeacher(request):
    teacher = Teacher.objects.all()
    serializer = TeacherSerializer(teacher, many=True)
    return Response(serializer.data)





