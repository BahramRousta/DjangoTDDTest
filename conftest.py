import pytest
from django.test import Client
from todo.models import Todo


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def todo():
    return Todo.objects.create(name='something')