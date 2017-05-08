from django.contrib.auth.models import User
from django.shortcuts import reverse

from rest_framework.test import APITestCase

from api.models import Note


class TestNoteApi(APITestCase):
    def setUp(self):
        # create user
        self.user = User.objects.create_user(username="amos", email="amos.omondi@andela.com", password="test")

        # create note
        self.note = Note(name="Test Note 1", content="A bright day", owner=self.user)
        self.note.save()

        # login to the api
        self.client.login(username="amos", password="test")

    def test_note_creation(self):
        response = self.client.post(reverse('notes'), {
            'name': 'New Note',
            'content': 'A new note'
        })

        self.assertEqual(Note.objects.count(), 2)
        self.assertEqual(201, response.status_code)

    def test_getting_notes(self):
        response = self.client.get(reverse('notes'), format="json")
        self.assertEqual(len(response.data['results']), 1)

    def test_note_update(self):
        response = self.client.put(reverse('detail', kwargs={'pk': 1}), {
            'name': 'Test Note 1 updated',
            'content': 'Totally new content'
        }, format="json")

        self.assertEqual('Test Note 1 updated', response.data['name'])

    def test_note_deletion(self):
        response = self.client.delete(reverse('detail', kwargs={'pk': 1}))

        self.assertEqual(204, response.status_code)
