from rest_framework import serializers
from . import models
from .models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['name', 'email', 'address', 'phone', 'created_at']


    def create(self, validated_data):
        user = School(

            name=self.validated_data['name'],
            email=self.validated_data['email'],
            address=self.validated_data['address'],
            phone=self.validated_data['phone'],


        )

        user.save()
        return user

