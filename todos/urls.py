from django.urls import path
from .views import TagView, TaskView

urlpatterns = [
    path('<int:pk>/', TagView.as_view()),
    path('', TaskView.as_view()),
]