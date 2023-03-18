from rest_framework.generics import ListAPIView
from .models import Todo
from .serializers import TodosListSerializer


class TodosListView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodosListSerializer
