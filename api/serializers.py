from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'name', 'content', 'owner')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # make sure password is not returned on read
        extra_kwargs = {
            'password': {'write_only': True}
        }
