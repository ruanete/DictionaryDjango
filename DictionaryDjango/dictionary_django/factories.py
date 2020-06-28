import factory
from faker import Factory
from django.contrib.auth.models import User
from .models import term, definition

faker = Factory.create()


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence('testuser{}'.format)
    email = factory.Sequence('testuser{}@company.com'.format)
    first_name = factory.Sequence('testfirstname'.format)
    last_name = factory.Sequence('testlastname'.format)


class TermFactory(factory.DjangoModelFactory):
    class Meta:
        model = term

    word = faker.word()


class DefinitionFactory(factory.DjangoModelFactory):
    class Meta:
        model = definition

    meaning = faker.sentence()
    word_meaning_relationship = factory.SubFactory(TermFactory)
