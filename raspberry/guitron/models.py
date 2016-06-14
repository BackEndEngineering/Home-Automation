from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Monitor(models.Model):
    event_id = models.CharField(max_length=256)

    def __str__(self):
        return str(self.event_id)





class Area(models.Model):
    name = models.CharField(max_length=128)
    area_id = models.CharField(max_length=256)
    Description = models.CharField(max_length=256)

    def __str__(self):
        return str(self.name)



class Gadget(models.Model):
    gadget_id = models.CharField(max_length=256)
    ip_address = models.CharField(max_length=256)
    monitor = models.ForeignKey(Monitor, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.gadget_id)

class Pin(models.Model):
    pin_id = models.CharField(max_length=256)

    def __str__(self):
        return str(self.pin_id)

class Switch(models.Model):
    name = models.CharField(max_length=128)
    switch_id = models.CharField(max_length=256)

    def __str__(self):
        return str(self.name)


class Install(models.Model):
    name = models.CharField(max_length=128)
    customer = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    install_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.name)
