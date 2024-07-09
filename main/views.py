from django.shortcuts import render
from rest_framework.response import Response
from . serializer import AccessGrantTableSerializer
from . models import AccessGrantTable

from rest_framework.decorators import api_view
from rest_framework import status
from .tasks import *


# Create your views here.


@api_view(['GET', 'POST'])
def access_list(request):

    if request.method == 'GET' :
        
        access = AccessGrantTable.objects.all()
        serializer = AccessGrantTableSerializer(access, many=True)
        
        return Response(serializer.data)
        
        
    if request.method == 'POST':
    
        user = request.user
        data = request.data.copy()
        data['granted_by'] = user.username  # Add the current logged-in user's username
        serializer = AccessGrantTableSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            
            with open('ansible/vars.yml', 'w') as f:
                f.write(data['inventory'])
                
                
            identifier = data['user_or_group_identifier'].lower()
            grant_access_task.delay(data['user'] ,identifier )

            
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
@api_view(['GET', 'PUT', 'DELETE'])
def access_detail(request, id):

    try:
        access = AccessGrantTable.objects.get(id=id)
    except AccessGrantTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET' :
        
        
        serializer = AccessGrantTableSerializer(access)
        
        return Response(serializer.data)
        
        
    elif request.method == 'PUT':
    
        serializer = AccessGrantTableSerializer(access, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
    
        access.delete()
        return response(status=status.HTTP_204_NO_CONTENT)
          