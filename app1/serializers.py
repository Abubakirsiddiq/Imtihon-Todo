from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

