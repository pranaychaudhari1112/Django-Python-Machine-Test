from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class ClientList(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDetail(APIView):
    def get(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectList(APIView):
    def post(self, request, client_id):
        try:
            client = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(client=client)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectListForUser(APIView):
    def get(self, request):
        # This would filter the projects assigned to the logged-in user.
        user_projects = Project.objects.filter(users__contains=[{'name': 'Rohit'}])  # Example for a specific user
        serializer = ProjectSerializer(user_projects, many=True)
        return Response(serializer.data)
