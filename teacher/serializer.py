from rest_framework import serializers

from teacher.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'email', 'state']


    def create(self, validated_data):
        user=Teacher(
        name=validated_data['name'],
        email=validated_data['email'],
        state=validated_data['state'],
        )

        user.save()
        return user


