from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from Accounts.models import CustomUser,Faculte


class RegisterUserSerializer(serializers.ModelSerializer):
    faculte = serializers.PrimaryKeyRelatedField(queryset=Faculte.objects.all())

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'faculte', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        data = self.Meta.model(**validated_data)
        if password is not None:
            data.set_password(password)
        data.save()
        return data
    

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email']