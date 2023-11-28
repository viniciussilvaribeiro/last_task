from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import OwnerSerializer, LocalSerializer, EnviromentSerializer, DeviceSerializer
from .models import Owners, Locals, Enviroments, Devices


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

            owner = Owners.objects.get(pk = owner_id)

            local = Locals.objects.get(pk = local_id, owner = owner.id)

            serializer = LocalSerializer(local)

            return Response(serializer.data)
        
        except:

            return Response({'detail': "Don't found!"}, status = status.HTTP_404_NOT_FOUND)
        
    def post(self, request, owner_id):

        serializer = LocalSerializer(data = request.data)
    
        if serializer.is_valid():

            owner = Owners.objects.get(pk = owner_id)

            serializer.save(owner = owner)

            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, owner_id, local_id):

        try:

            owner = Owners.objects.get(pk = owner_id)

            local = Locals.objects.get(pk = local_id, owner = owner.id)

            local.delete()

            return Response(status = status.HTTP_204_NO_CONTENT)
    
        except:

            return Response({'detail': "Don't found!"}, status = status.HTTP_404_NOT_FOUND)


class EnviromentCreateViewRemove(APIView):

    def get(self, request, owner_id, local_id, enviroment_id):

        try:

            local = Locals.objects.get(pk = local_id, owner = owner_id)

            enviroment = Enviroments.objects.get(pk = enviroment_id, local = local.id)

            serializer = EnviromentSerializer(enviroment)

            return Response(serializer.data)
        
        except:

            return Response({'detail': "Don't found!"}, status = status.HTTP_404_NOT_FOUND)
        
    def post(self, request, owner_id, local_id):

        serializer = EnviromentSerializer(data = request.data)
    
        if serializer.is_valid():

            owner = Owners.objects.get(pk = owner_id)

            local = Locals.objects.get(pk = local_id, owner = owner.id)

            serializer.save(local = local)

            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, owner_id, local_id, enviroment_id):

        try:

            owner = Owners.objects.get(pk = owner_id)

            local = Locals.objects.get(pk = local_id, owner = owner.id)

            enviroment = Enviroments.objects.get(pk = enviroment_id, local = local.id)

            enviroment.delete()

            return Response(status = status.HTTP_204_NO_CONTENT)
    
        except:

            return Response({'detail': "Don't found!"}, status = status.HTTP_404_NOT_FOUND)


class DeviceCreateViewRemove(APIView):
    
    def get(self, request, owner_id, local_id, enviroment_id, device_id):

        try:

            owner = Owners.objects.get(pk = owner_id)

            local = Locals.objects.get(pk = local_id, owner = owner.id)

            enviroment = Enviroments.objects.get(pk = enviroment_id, local = local.id)

            device = Devices.objects.get(pk = device_id, enviroment = enviroment.id)

            serializer = DeviceSerializer(device)

            return Response(serializer.data)
        
        except:

            return Response({'detail': "Don't found!"}, status = status.HTTP_404_NOT_FOUND)
        
    def post(self, request, owner_id, local_id, enviroment_id):

        serializer = DeviceSerializer(data = request.data)
    
        if serializer.is_valid():

            owner = Owners.objects.get(pk = owner_id)

            local = Locals.objects.get(pk = local_id, owner = owner.id)

            enviroment = Enviroments.objects.get(pk = enviroment_id, local = local.id)

            serializer.save(enviroment = enviroment)

            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, owner_id, local_id, enviroment_id, device_id):

        try:

            owner = Owners.objects.get(pk = owner_id)

            local = Locals.objects.get(pk = local_id, owner = owner.id)

            enviroment = Enviroments.objects.get(pk = enviroment_id, local = local.id)

            device = Devices.objects.get(pk = device_id, enviroment = enviroment.id)

            device.delete()

            return Response(status = status.HTTP_204_NO_CONTENT)
        
        except:

            return Response({'detail': "Don't found!"}, status = status.HTTP_404_NOT_FOUND)