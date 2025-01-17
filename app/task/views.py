from rest_framework import viewsets

from app.task.models import Task
from app.task.serializer import TaskSerializer
# Create your views here.

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()