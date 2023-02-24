from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model
from .models import Work,Artist

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", )


class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Work
        fields='__all__'

        
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artist
        fields='__all__'