from django.urls import path
from .views import TodosListView

urlpatterns = [
    path('todos_list/', TodosListView.as_view(), name='todos-list')
]

