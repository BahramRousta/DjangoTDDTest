from django.urls import path
from .views import TodosListView, CreateTodoView

urlpatterns = [
    path('todos_list/', TodosListView.as_view(), name='todos-list'),
    path('create_todo/', CreateTodoView.as_view(), name='create-todo'),
]

