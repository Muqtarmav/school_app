from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

from . import serializer
from . import models
from .models import Student
from .serializer import StudentSerializer


@api_view(['POST'])
def createStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getStudentList(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getStudentId(request, pk):
    student = Student.objects.all(id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(request)

@api_view(['DELETE'])
def studentUpdate(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return Response(serializer.data)


@api_view(['POST'])
def updateView(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()

    return Response(serializer.data)
