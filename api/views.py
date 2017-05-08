from django.contrib.auth.models import User

from rest_framework.generics import ListCreateAPIView, CreateAPIView

from api.models import Note
from api.serializers import UserSerializer, NoteSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        username = self.request.data['username']
        email = self.request.data['email']
        password = self.request.data['password']

        User.objects.create_user(username=username, email=email, password=password)


class NoteCreateView(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetailView():
    pass
