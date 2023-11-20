from django.urls import path
from .views import task_list, add_task, delete_task, deactivate_task

urlpatterns = [
    path('', task_list, name='task-list'),
    path('add/', add_task, name='add-task'),
    path('delete/<int:pk>', delete_task, name='task-delete'),
    path('deactivate/<int:task_id>/', deactivate_task, name='deactivate-task'),
]