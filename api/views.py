from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Note
from api.serializers import UserSerializer, NoteSerializer
from api.permissions import IsOwner


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
    permission_classes = (IsOwner,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get_queryset(self):
    #     return get_object_or_404(Note, owner=self.request.user)


class NoteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsOwner,)
