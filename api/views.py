from django.shortcuts import render
from django.http import JsonResponse
# restframework import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Task
from .serializers import TaskSerializer
# Create your views here.


class apiOverview(APIView):
    def get(self, request, format=None):
        api_urls = {
            'List': '/task-list/',
            'Detail View': '/task-detail/<str:pk>/',
            'Create': '/task-create/',
            'Update': '/task-update/<str:pk>/',
            'Delete': '/task-delete/<str:pk>/',
        }
        return Response(api_urls)


class taskList(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class taskDetail(APIView):
    def get(self, request, pk, format=None):
        tasks = Task.objects.get(id=pk)
        serializer = TaskSerializer(tasks, many=False)
        return Response(serializer.data)


class taskCreate(APIView):
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class taskupdate(APIView):
    def put(self, request, pk, format=None):
        tasks = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=tasks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class taskDelete(APIView):
    def delete(self, request, pk, format=None):
        tasks = Task.objects.get(id=pk)
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
