from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from users.models import SKILLS

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200, allow_blank=True)
    last_name = serializers.CharField(max_length=200, allow_blank=True)
    email = serializers.CharField(max_length=200, allow_blank=True)
    password = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=200, allow_blank=True)
    cv = serializers.CharField(max_length=200, allow_blank=True)
    state = serializers.CharField(max_length=200, allow_blank=True)
    interview_notes = serializers.CharField(max_length=2000, allow_blank=True)
    feedback_for_mentors = serializers.CharField(max_length=2000, allow_blank=True)
    mentor_comments = serializers.CharField(max_length=2000, allow_blank=True)
    position = serializers.CharField(max_length=200,allow_blank=True)
    skills = serializers.MultipleChoiceField(choices=SKILLS, allow_blank=True)
    status = serializers.CharField(max_length=200, allow_blank=True)
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email',instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.cv = validated_data.get('cv', instance.cv)
        instance.state = validated_data.get('state', instance.state)
        instance.interview_notes = validated_data.get('interview_notes', instance.interview_notes)
        instance.feedback_for_mentors = validated_data.get('feedback_for_mentors', instance.feedback_for_mentors)
        instance.mentor_comments = validated_data.get('mentor_comments', instance.mentor_comments)
        instance.status = validated_data.get('status', instance.status)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.position = validated_data.get('position', instance.position)

        if "password" in validated_data.keys():
            instance.password = make_password(validated_data.get('password'))
        instance.save()
        return instance
    
    
class RestrictedCustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200, read_only=True)
    first_name = serializers.CharField(max_length=200, read_only=True)
    last_name = serializers.CharField(max_length=200, read_only=True)
    email = serializers.CharField(max_length=200, read_only=True)
    password = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=200, read_only=True)
    cv = serializers.CharField(max_length=200, read_only=True)
    state = serializers.CharField(max_length=200, read_only=True)
    interview_notes = serializers.CharField(max_length=2000, read_only=True)
    feedback_for_mentors = serializers.CharField(max_length=2000, read_only=True)
    mentor_comments = serializers.CharField(max_length=2000, read_only=True)
    position = serializers.CharField(max_length=200, read_only=True)
    skills = serializers.MultipleChoiceField(choices=SKILLS, read_only=True)
    status = serializers.CharField(max_length=200, read_only=True)
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if "password" in validated_data.keys():
            instance.password = make_password(validated_data.get('password'))
        instance.save()
        return instance
