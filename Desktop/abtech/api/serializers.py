from dataclasses import fields
from rest_framework import serializers
from .models import Task, Teams
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
 
class userSerializers(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields =  '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'