from rest_framework import serializers
from .models import Student 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id" ,"name" , "email" ,"branch" , "created_at"]
        read_only_field = ["id" , "created_at"]

        # Serializers Validation

        def validate_name(self, value):
            if len(value) < 3:
                raise serializers.ValidationError("Name must be at least 3 characters long.")
            return value