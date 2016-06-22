from django.db import models
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta
from django import forms
from datetime import date
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

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

class Controller(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    uuid = models.UUIDField(unique=True, null=False, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.id)

class Component(models.Model):
    name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    controller = models.ForeignKey(Controller, models.SET_NULL, null=True)
    pin = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id)

class Event(models.Model):
    component = models.ForeignKey(Component, models.SET_NULL, null=True)
    time = models.DateField(auto_now_add=True, db_index=True)
    value = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)

class Gadget(models.Model):
    gadget_id = models.CharField(max_length=256)
    ip_address = models.CharField(max_length=256)

    def __str__(self):
        return str(self.gadget_id)

class Light(models.Model):
    on = models.CharField(max_length=256)
    off = models.CharField(max_length=256)

    def __str__(self):
        return str(self.on)

class Pin(models.Model):
    pin_id = models.CharField(max_length=256)
    signal = models.CharField(max_length=256)

    def __str__(self):
        return str(self.pin_id)

class Switch(models.Model):
    name = models.CharField(max_length=128)
    switch_id = models.CharField(max_length=256)
    pin = models.OneToOneField('Pin', null=True)

    def __str__(self):
        return str(self.name)

class Install(models.Model):
    name = models.CharField(max_length=128)
    customer = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    install_date = models.DateField(blank=True, null=True)

    @property
    def age(self):
        return relativedelta(date.today(), self.install_date)

    def __str__(self):
        return str(self.name)

class GadgetForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()

    def __str__(self):
        return str(self.subject)

class Image(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(null=True, blank=True,
            width_field="width_field",
            height_field="height_field")
