from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user, created = User.objects.update_or_create(
            username=validated_data.pop('username'),
            password=make_password(validated_data.pop('password'))
        )

        return user


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Client
        fields = ('user', 'email', 'first_name', 'last_name', 'points', 'birth_date')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        client, created = Client.objects.update_or_create(
            user=user,
            email=validated_data.pop('email'),
            first_name=validated_data.pop('first_name'),
            last_name=validated_data.pop('last_name'),
            points=validated_data.pop('points'),
            birth_date=validated_data.pop('birth_date')
        )

        return client


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = ('name', 'longitude', 'latitude')


class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    establishment = EstablishmentSerializer(required=True)

    class Meta:
        model = Admin
        fields = ('user', 'establishment', 'name')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        establishment_data = validated_data.pop('establishment')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        establishment = EstablishmentSerializer.create(EstablishmentSerializer(), validated_data=establishment_data)
        admin, created = Admin.objects.update_or_create(
            user=user,
            establishment=establishment,
            name=validated_data.pop('name')
        )

        return admin
