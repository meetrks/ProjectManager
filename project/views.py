from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from project.models import Project
from project.serializers import ProjectSerializer


class ProjectView(GenericAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_list(self, request):
        queryset = self.get_queryset()
        return render(request, 'project/list_view.html', {"responses": queryset})

    def get(self, request, project_id=None):
        if project_id is None:
            return self.get_list(request)
        query = self.get_queryset().filter(pk=project_id).first()
        if not query:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        return render(request, 'project/index.html', {"response": query})

    @method_decorator(permission_required('project.add_project'))
    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=request.user)
            return redirect('/')

    @method_decorator(permission_required('project.update_project'))
    def put(self, request, project_id):
        instance = Project.objects.get(pk=project_id)
        if request.data.get('is_deleted'):
            instance.delete()
            return Response({}, status=status.HTTP_200_OK)
        serializer = self.get_serializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectCreateView(GenericAPIView):

    @method_decorator(permission_required('project.add_project'))
    def get(self, request):
        return render(request, 'project/create_project.html')


class ProjectUpdateView(GenericAPIView):
    @method_decorator(permission_required('project.update_project'))
    def get(self, request, project_id):
        instance = Project.objects.get(pk=project_id)
        return render(request, 'project/update_project.html', {"instance": instance})
