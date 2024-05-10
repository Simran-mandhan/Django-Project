# urls.py

from django.urls import path
from .views import TaskListView, TaskRetrieveView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskRetrieveView.as_view(), name='task-retrieve'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]