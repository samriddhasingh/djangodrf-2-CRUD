from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=1000)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=1000)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.city=validated_data.get('city',instance.city)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.save()
        return instance