from rest_framework import serializers


# class UserModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class ProfileSerializer(serializers.Serializer):
    patronymic_name = serializers.CharField(max_length=150)
    birth_date = serializers.DateField()
    sex = serializers.CharField(max_length=1)
    edited_date = serializers.DateTimeField()


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    details = ProfileSerializer(source='profile', required=False)
