import pytest
from ..models import Todo


class TestModel:

    def test_should_be_create_instance(self, db):
        Todo.objects.create(name="something")
        assert Todo.objects.count() == 1

    def test_should_repr_instance(self, db):
        todo = Todo.objects.create(name="something")
        assert str(todo) == "something"

