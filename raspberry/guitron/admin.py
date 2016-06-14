from django.contrib import admin
from .models import Install, Area, Pin, Switch, Gadget, Monitor
# Register your models here.
#class DeviceAdmin(admin.ModelAdmin):
#    pass

#class EventAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Monitor)
admin.site.register(Gadget)
admin.site.register(Install)
admin.site.register(Area)
admin.site.register(Pin)
admin.site.register(Switch)
