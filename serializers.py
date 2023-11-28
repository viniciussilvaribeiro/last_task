from rest_framework.serializers import ModelSerializer
from .models import Locals, Enviroments, Devices, Owners


class OwnerSerializer(ModelSerializer):


    class Meta:

        model = Owners

        fields = '__all__'


class LocalSerializer(ModelSerializer):


    class Meta:

        model = Locals

        fields = ['name', 'description', 'color']


class EnviromentSerializer(ModelSerializer):


    class Meta:

        model = Enviroments

        fields = ['name', 'description', 'color']


class DeviceSerializer(ModelSerializer):


    class Meta:

        model = Devices

        fields = ['name', 'description', 'color']