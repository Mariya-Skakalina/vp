from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    text = serializers.CharField()
    public_comment = serializers.IntegerField()


class AnswerSerializer(serializers.Serializer):
    text = serializers.CharField()
    answer = serializers.IntegerField()


class RatingSerializer(serializers.Serializer):
    public = serializers.IntegerField(required=False)
    like = serializers.BooleanField(default=False)
    comment = serializers.IntegerField(required=False)