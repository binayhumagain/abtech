import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, TeamSerializer
from .models import Task, Teams
from rest_framework.renderers import JSONRenderer

@api_view(['GET'])
def apiOverview (request):

    api_urls={
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>',
    }
    return Response (api_urls)

def homeView (request):
    return render(request, 'api/home.html')

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')  #Aru function jasari garda ni huncha, yeha content type pass garya cha

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance = task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
        
    return Response('Item successfully deleted')

@api_view(['GET'])
def teams(request):
    tasks = Teams.objects.all()
    serializer = TeamSerializer(tasks, many=True)
    return Response(serializer.data)