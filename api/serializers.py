from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer

from api.models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'name', 'content', 'owner')
        extra_kwargs = {
            'owner': {'read_only': True}
        }


class UserSerializer(ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'notes')
        # make sure password is not returned on read
        extra_kwargs = {
            'password': {'write_only': True}
        }
