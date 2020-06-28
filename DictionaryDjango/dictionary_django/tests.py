import unittest
from django.urls import reverse
from django.test import Client
from .models import definition
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from .factories import DefinitionFactory, TermFactory


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


term_object = TermFactory()
definition_object = DefinitionFactory(word_meaning_relationship=term_object)


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
            "word": term_object.word,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_detail_term(self):
        url = reverse('dictionary_django_term_detail', args=[term_object.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_remove_term(self):
        url = reverse('dictionary_django_term_remove', args=[term_object.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_term(self):
        data = {
            "word": term_object.word,
        }
        url = reverse('dictionary_django_term_update', args=[term_object.pk,])
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
            "meaning": definition_object.meaning,
            "word_meaning_relationship": definition_object.word_meaning_relationship.pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_definition(self):
        url = reverse('dictionary_django_definition_detail', args=[definition_object.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_remove_definition(self):
        url = reverse('dictionary_django_definition_remove', args=[definition_object.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_definition(self):
        data = {
            "meaning": definition_object.meaning,
            "word_meaning_relationship": definition_object.word_meaning_relationship.pk,
        }
        url = reverse('dictionary_django_definition_update', args=[definition_object.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


