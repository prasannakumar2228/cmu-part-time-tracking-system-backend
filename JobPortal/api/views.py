from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from.serializers import StudentSerializer
from django.contrib.auth.models import User

from UserProfiles.models import Student,Manager
@api_view(['GET'])
def GetRoutes(request):
    routes=[
        {'GET':'/api/users'},
        {'GET':'/api/users/id'}
    ]
    return Response(routes)
@api_view(['GET','POST','PUT'])

def getStudents(request):
    if request.method == 'GET':
        users = Student.objects.all()
        serializer = StudentSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method=='PUT':
        username=request.data.get('username')
        try:
            user=Student.objects.get(username=username)
        except Student.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PUT'])
def getManagers(request):
    if request.method == 'GET':
        users = Manager.objects.all()
        serializer = StudentSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method=='PUT':
        username=request.data.get('username')
        try:
            user=Manager.objects.get(username=username)
        except Manager.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)