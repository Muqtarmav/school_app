from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'age', 'state']

        def create(self, validated_data):
            user = Student(

                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                email=validated_data['email'],
                age=validated_data['age'],
                state=validated_data['state']

            )

            user.save()
            return user









