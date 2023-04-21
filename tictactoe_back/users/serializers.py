from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


# class UserModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('patronymic_name', 'birth_date', 'sex', 'edited_date')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        # Unless the application properly enforces that this field is
        # always set, the following could raise a `DoesNotExist`, which
        # would need to be handled.
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        profile.patronymic_name = profile_data.get(
            'patronymic_name',
            profile.patronymic_name
        )
        profile.birth_date = profile_data.get(
            'birth_date',
            profile.birth_date
        )
        profile.sex = profile_data.get(
            'sex',
            profile.sex
        )
        profile.edited_date = profile_data.get(
            'edited_date',
            profile.edited_date
        )
        profile.save()

        return instance
