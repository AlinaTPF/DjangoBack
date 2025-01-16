from rest_framework import viewsets

from task.models import Task
from task.serializer import TaskSerializer
# Create your views here.

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()