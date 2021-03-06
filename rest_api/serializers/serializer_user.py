from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    nickname = serializers.CharField(min_length=3, max_length=50, required=True, trim_whitespace=True)
    email = serializers.EmailField(min_length=6, max_length=50, required=True)
    password = serializers.CharField(min_length=8, max_length=30, required=True)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=6, max_length=50, required=True)
    password = serializers.CharField(min_length=8, max_length=30, required=True)


class UserSettingSerializer(serializers.Serializer):
    nickname = serializers.CharField(min_length=3, max_length=50, required=True)
    email = serializers.EmailField(min_length=6, max_length=50, required=True)
    about_oneself = serializers.CharField(allow_blank=True)
    partner = serializers.BooleanField(allow_null=False, required=True)