from .models import Users
from rest_framework import serializers
from .validation import file_size


class Userserializer(serializers.ModelSerializer):
    photo=serializers.FileField(required=False,validators=[file_size])
    class Meta:
        model=Users
        fields='__all__'
    

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)
