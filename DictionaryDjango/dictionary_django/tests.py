import unittest
from django.urls import reverse
from django.test import Client
from .models import term, definition
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_term(**kwargs):
    defaults = {}
    defaults["word"] = "word"
    defaults.update(**kwargs)
    return term.objects.create(**defaults)


def create_definition(**kwargs):
    defaults = {}
    defaults["meaning"] = "meaning"
    defaults.update(**kwargs)
    if "word_meaning_relationship" not in defaults:
        defaults["word_meaning_relationship"] = create_term()
    return definition.objects.create(**defaults)


class termViewTest(unittest.TestCase):
    '''
    Tests for term
    '''
    def setUp(self):
        self.client = Client()

    def test_list_term(self):
        url = reverse('dictionary_django_term_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_term(self):
        url = reverse('dictionary_django_term_create')
        data = {
            "word": "word",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_term(self):
        term = create_term()
        url = reverse('dictionary_django_term_detail', args=[term.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_term(self):
        term = create_term()
        data = {
            "word": "word",
        }
        url = reverse('dictionary_django_term_update', args=[term.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class definitionViewTest(unittest.TestCase):
    '''
    Tests for definition
    '''
    def setUp(self):
        self.client = Client()

    def test_list_definition(self):
        url = reverse('dictionary_django_definition_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_definition(self):
        url = reverse('dictionary_django_definition_create')
        data = {
            "meaning": "meaning",
            "word_meaning_relationship": create_term().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_definition(self):
        definition = create_definition()
        url = reverse('dictionary_django_definition_detail', args=[definition.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_definition(self):
        definition = create_definition()
        data = {
            "meaning": "meaning",
            "word_meaning_relationship": create_term().pk,
        }
        url = reverse('dictionary_django_definition_update', args=[definition.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


