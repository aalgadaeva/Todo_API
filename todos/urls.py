from django.urls import path
from .views import TagView, TaskList, TaskDetail

urlpatterns = [
    path('tags/<int:pk>/', TagView.as_view()),
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
]