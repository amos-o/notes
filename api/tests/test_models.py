from django.test import TestCase

from django.contrib.auth.models import User

from api.models import Note


class TestNoteModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="amos", email="amos.omondi@andela.com", password="test")

        self.note = Note(name="Test Note", content="Test Note content", owner=self.user)
        self.note.save()


    def test_note_creation(self):
        note2 = Note(name="Test Note 2", content="Test Note 2 content", owner=self.user)
        note2.save()

        self.assertEqual(Note.objects.count(), 2)

    def test_note_representation(self):
        self.assertEqual(self.note.name, str(self.note))
