from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import OwnerSerializer, LocalSerializer
from .models import Owners, Locals


class OwnerCreateView(APIView):

    def get(self, request, owner_id):

        try:

            owner = Owners.objects.get(pk = owner_id)

            serializer = OwnerSerializer(owner)

            return Response(serializer.data)
        
        except:

            return Response({'detail': "Don't found!"}, status = status.HTTP_404_NOT_FOUND)

    def post(self, request):

        serializer = OwnerSerializer(data = request.data)
    
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class LocalCreateViewRemove(APIView):
    
    def get(self, request, owner_id, local_id):

        try:

            local = Locals.objects.get(pk = local_id, owner = owner_id)

            serializer = LocalSerializer(local)

            return Response(serializer.data)
        
        except:

            return Response({'detail': "Don't found!"}, status = status.HTTP_404_NOT_FOUND)
        
    def post(self, request, owner_id):

        serializer = LocalSerializer(data = request.data)
    
        if serializer.is_valid():

            owner = get_object_or_404(Owners, id = owner_id)

            serializer.save(owner = owner)

            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, owner_id, local_id):

        owner = get_object_or_404(Owners, id = owner_id)

        local = get_object_or_404(Locals, id = local_id)

        local.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)