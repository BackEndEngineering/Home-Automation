from django.contrib import admin
from .models import Install, Area, Pin, Switch, Gadget, Monitor, Controller, Component, Event, Action

class ControllerAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)

admin.site.register(Monitor)
admin.site.register(Action)
admin.site.register(Controller, ControllerAdmin)
admin.site.register(Component)
admin.site.register(Event)
admin.site.register(Gadget)
admin.site.register(Install)
admin.site.register(Area)
admin.site.register(Pin)
admin.site.register(Switch)
