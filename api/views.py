from django.shortcuts import render
# from rest_framework import generics
from rest_framework import viewsets
from todos import models
from . import serializers
# Create your views here.

# class ListTodo(generics.ListCreateAPIView):
#     queryset=models.Todo.objects.all()
#     serializer_class=serializers.TodoSerializer

# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     queryset=models.Todo.objects.all()
#     serializer_class= serializers.TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset= models.Todo.objects.all()
    serializer_class=serializers.TodoSerializer