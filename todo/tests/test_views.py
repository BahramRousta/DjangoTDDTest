from django.urls import reverse
from todo.models import Todo


class TestCreateTodo:

    def test_should_get_todos_list_view(self, db, client):
        url = reverse('todos-list')
        response = client.get(url)
        assert response.status_code == 200

    def test_should_retrieve_todos_list(self, db, client, todo):
        url = reverse('todos-list')
        client.get(url)
        assert Todo.objects.count() == 1