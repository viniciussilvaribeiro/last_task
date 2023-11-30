from django.db import models


class Owners(models.Model):

    name = models.CharField(max_length = 30)


class Locals(models.Model):
    
    name = models.CharField(max_length = 30)

    description = models.CharField(max_length = 100)

    color = models.CharField(max_length = 15)

    owner = models.ForeignKey('Owners', on_delete = models.PROTECT, related_name = 'locals')


class Enviroments(models.Model):
    
    name = models.CharField(max_length = 30)

    description = models.CharField(max_length = 100)

    color = models.CharField(max_length = 15)

    local = models.ForeignKey('Locals', on_delete = models.PROTECT, related_name = 'enviroments')


class Devices(models.Model):
    
    name = models.CharField(max_length = 30)

    description = models.CharField(max_length = 100)

    online = models.BooleanField(default = False)

    on = models.BooleanField(default = False)

    color = models.CharField(max_length = 15)

    enviroment = models.ForeignKey('Enviroments', on_delete = models.PROTECT, related_name = 'devices')