from rest_framework import serializers
from todo.models import Todo


class TodosListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['name']
