from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import OwnerSerializer, LocalSerializer, EnviromentSerializer, DeviceSerializer
from .models import Owners, Locals, Enviroments, Devices


def pathfinder(**kargs):

    try:

        owner = Owners.objects.get(pk = kargs.get('owner_id'))

        if kargs.get('local_id'):

            try:

                local = Locals.objects.get(pk = kargs.get('local_id'), owner = owner.id)

            except:

                return Locals.DoesNotExist

            if kargs.get('enviroment_id'):

                try:

                    enviroment = Enviroments.objects.get(pk = kargs.get('enviroment_id'), local = local.id)

                except:

                    return Enviroments.DoesNotExist

                if kargs.get('device_id'):

                    try:

                        device = Devices.objects.get(pk = kargs.get('device_id'), enviroment = enviroment.id)

                        serializer = DeviceSerializer(device)

                        return serializer
                    
                    except:

                        return Devices.DoesNotExist

                serializer = EnviromentSerializer(enviroment)

                return serializer
            
            serializer = LocalSerializer(local)

            return serializer
        
        serializer = OwnerSerializer(owner)

        return serializer
    
    except:

        return Owners.DoesNotExist


def authenticator(object):

    if object == Owners.DoesNotExist:

        return Response({'detail': "Owner don't found!"}, status = status.HTTP_404_NOT_FOUND)
    
    elif object == Locals.DoesNotExist:

        return Response({'detail': "Local don't found!"}, status = status.HTTP_404_NOT_FOUND)
    
    elif object == Enviroments.DoesNotExist:

        return Response({'detail': "Enviroment don't found!"}, status = status.HTTP_404_NOT_FOUND)
    
    elif object == Devices.DoesNotExist:

        return Response({'detail': "Device don't found!"}, status = status.HTTP_404_NOT_FOUND)
    
    else:

        return Response(object.data, status = status.HTTP_200_OK)
    

class OwnerCreateView(APIView):

    def get(self, request, owner_id):

        return_object = pathfinder(owner_id = owner_id)

        return authenticator(return_object)

    def post(self, request):

        serializer = OwnerSerializer(data = request.data)
        
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        else:

            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class LocalCreateViewRemove(APIView):
    
    def get(self, request, owner_id, local_id):

            return_object = pathfinder(owner_id = owner_id, local_id = local_id)

            return authenticator(return_object)
        
    def post(self, request, owner_id):

        try:

            owner = Owners.objects.get(pk = owner_id)

            serializer = LocalSerializer(data = request.data)

            if serializer.is_valid():

                serializer.save(owner = owner)

                serializer.save()

                return Response(serializer.data, status = status.HTTP_201_CREATED)
            
            else:

                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
        except Owners.DoesNotExist:

            return Response({'detail': "Owner don't found!"}, status = status.HTTP_404_NOT_FOUND)
    
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

        return_object = pathfinder(owner_id = owner_id, local_id = local_id, enviroment_id = enviroment_id)
        
        return authenticator(return_object)        
        
    def post(self, request, owner_id, local_id):
        
        try:

            owner = Owners.objects.get(pk = owner_id)

            local = Locals.objects.get(pk = local_id, owner = owner.id)

            serializer = EnviromentSerializer(data = request.data)

            if serializer.is_valid():

                serializer.save(local = local)

                serializer.save()

                return Response(serializer.data, status = status.HTTP_201_CREATED)
            
            else:

                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
        except Owners.DoesNotExist:

            return Response({'detail': "Owner don't found!"}, status = status.HTTP_404_NOT_FOUND)
    
        except Locals.DoesNotExist:

            return Response({'detail': "Local don't found!"}, status = status.HTTP_404_NOT_FOUND)
    
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

        return_object = pathfinder(owner_id = owner_id, local_id = local_id, enviroment_id = enviroment_id, device_id = device_id)

        return authenticator(return_object)

    def post(self, request, owner_id, local_id, enviroment_id):

        try:

            owner = Owners.objects.get(pk = owner_id)

            local = Locals.objects.get(pk = local_id, owner = owner.id)

            enviroment = Enviroments.objects.get(pk = enviroment_id, local = local.id)

            serializer = DeviceSerializer(data = request.data)

            if serializer.is_valid():

                serializer.save(enviroment = enviroment)

                serializer.save()

                return Response(serializer.data, status = status.HTTP_201_CREATED)
            
            else:

                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
        except Owners.DoesNotExist:

            return Response({'detail': "Owner don't found!"}, status = status.HTTP_404_NOT_FOUND)
    
        except Locals.DoesNotExist:

            return Response({'detail': "Local don't found!"}, status = status.HTTP_404_NOT_FOUND)
    
        except Enviroments.DoesNotExist:

            return Response({'detail': "Enviroment don't found!"}, status = status.HTTP_404_NOT_FOUND)
    
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
        

class DeviceOnOffLine(APIView):

    def put(self, request, owner_id, local_id, enviroment_id, wish):

        owner = Owners.objects.get(pk = owner_id)

        local = Locals.objects.get(pk = local_id, owner = owner.id)

        enviroment = Enviroments.objects.get(pk = enviroment_id, local = local.id)

        devices = Devices.objects.filter(enviroment = enviroment.id, on = True)

        devices.update(online = bool(wish))

        serializer = DeviceSerializer(devices, many = True)

        return Response(serializer.data)
        

class DeviceOnOff(APIView):

    def put(self, request, owner_id, local_id, enviroment_id, wish):

        owner = Owners.objects.get(pk = owner_id)

        local = Locals.objects.get(pk = local_id, owner = owner.id)

        enviroment = Enviroments.objects.get(pk = enviroment_id, local = local.id)

        devices = Devices.objects.filter(enviroment = enviroment.id)
            
        devices.update(on = bool(wish))

        serializer = DeviceSerializer(devices, many = True)

        return Response(serializer.data)
        

class DeviceOnOffLineById(APIView):

    def put(self, request, owner_id, local_id, enviroment_id, device_id, wish):

        owner = Owners.objects.get(pk = owner_id)

        local = Locals.objects.get(pk = local_id, owner = owner.id)

        enviroment = Enviroments.objects.get(pk = enviroment_id, local = local.id)

        device = Devices.objects.get(id = device_id, enviroment = enviroment.id, on = True)

        device.online = bool(wish)

        device.save()

        serializer = DeviceSerializer(device)

        return Response(serializer.data)
        

class DeviceOnOffById(APIView):

    def put(self, request, owner_id, local_id, enviroment_id, device_id, wish):

        owner = Owners.objects.get(pk = owner_id)

        local = Locals.objects.get(pk = local_id, owner = owner.id)

        enviroment = Enviroments.objects.get(pk = enviroment_id, local = local.id)

        device = Devices.objects.get(id = device_id, enviroment = enviroment.id)

        device.on = bool(wish)

        device.save()

        serializer = DeviceSerializer(device)

        return Response(serializer.data)
    

class LocalTurnOnOffLineDevices(APIView):
    
    def put(self, request, owner_id, local_id, wish):

        owner = Owners.objects.get(pk = owner_id)

        local = Locals.objects.get(pk = local_id, owner = owner.id)

        enviroments = local.enviroments.all()

        device_list_resonse = []

        for enviroment in enviroments:

            for device in enviroment.devices.all():

                device.online = bool(wish)

                device.save()

                device_list_resonse.append(device)

        serializer = DeviceSerializer(device_list_resonse, many = True)

        return Response(serializer.data, status = status.HTTP_201_CREATED)


class LocalTurnOnOffDevices(APIView):
    
    def put(self, request, owner_id, local_id, wish):

        owner = Owners.objects.get(pk = owner_id)

        local = Locals.objects.get(pk = local_id, owner = owner.id)

        enviroments = local.enviroments.all()

        device_list_resonse = []

        for enviroment in enviroments:

            for device in enviroment.devices.all():

                device.on = bool(wish)

                device.save()

                device_list_resonse.append(device)

        serializer = DeviceSerializer(device_list_resonse, many = True)

        return Response(serializer.data, status = status.HTTP_201_CREATED)