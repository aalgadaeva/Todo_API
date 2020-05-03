from rest_framework import generics
from .serializers import TaskSerializer, TagSerializer     
from .models import Task, Tag 

class TagView(generics.RetrieveUpdateDestroyAPIView):       
    serializer_class = TagSerializer          
    queryset = Tag.objects.all()

class TaskList(generics.ListCreateAPIView):       
    serializer_class = TaskSerializer          
    queryset = Task.objects.all() 
    filterset_fields = ['creation_date', 'finish_date','status', 'tags']

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

