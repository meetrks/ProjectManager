from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from task.models import Task
from task.serializers import TaskSerializer


class TaskView(GenericAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()

    def get(self, request, project_id, task_id):

        query = self.get_queryset().filter(pk=task_id, project_id=project_id).first()
        if not query:
            return render(request, 'base/404.html')
        users = User.objects.all()
        return render(request, 'task/index.html', {"response": query, "users": users})

    @method_decorator(permission_required('task.add_task'))
    def post(self, request, project_id):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(project_id=project_id)
            return redirect('/project/' + project_id)

    @method_decorator(permission_required('task.update_task'))
    def put(self, request, project_id, task_id):
        instance = Task.objects.get(pk=task_id, project_id=project_id)
        if request.data.get('is_deleted'):
            instance.delete()
            return Response({}, status=status.HTTP_200_OK)
        serializer = self.get_serializer(data=request.data, instance=instance, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class TaskCreateView(GenericAPIView):
    @method_decorator(permission_required('task.add_task'))
    def get(self, request, project_id):
        users = User.objects.all()
        return render(request, 'task/create_task.html', {"project_id": project_id, "users": users})


class TaskUpdateView(GenericAPIView):
    @method_decorator(permission_required('task.update_task'))
    def get(self, request, project_id, task_id):
        instance = Task.objects.get(pk=task_id, project_id=project_id)
        users = User.objects.all()
        return render(request, 'task/update_task.html', {"instance": instance, "users": users})
