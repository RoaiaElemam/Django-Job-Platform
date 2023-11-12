from rest_framework import serializers
from .models import Job

#python----->jesson

class JobSerializer(serializers.ModelSerializer):
     class Meta:
        model=Job
        #fields='__all__'
        exclude=('location',)