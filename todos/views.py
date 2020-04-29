# from rest_framework import filters, viewsets  
# from django_filters import rest_framework as filters 
# from rest_framework.filters import DjangoFilterBackend
# from .filters import TaskFilter    
from rest_framework import generics
from .serializers import TaskSerializer, TagSerializer     
from .models import Task, Tag 

class TagView(generics.RetrieveAPIView):       
    serializer_class = TagSerializer          
    queryset = Tag.objects.all()

class TaskView(generics.ListAPIView):       
    serializer_class = TaskSerializer          
    queryset = Task.objects.all() 
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = TaskFilter

