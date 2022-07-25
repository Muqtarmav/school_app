from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from school.models import School
from school.serializer import SchoolSerializer


@api_view(['POST'])
def createSchool(request):
    serializer= SchoolSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def listSchool(request):
    school = School.objects.all()
    serializer = SchoolSerializer(school, many=True)
    return Response(serializer.data)