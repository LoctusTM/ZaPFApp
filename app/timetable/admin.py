from django.contrib import admin

from .models import Timeslot, Room, AKSlot, AK, RoomAssignment, News

class AKAdmin(admin.ModelAdmin):
    list_display = ('akslot', 'name', 'short', 'responsible', 'room', 'url', 'backup', 'public_id', 'published', 'kleine_fachschaften')
    
admin.site.register(Timeslot)
admin.site.register(Room)
admin.site.register(AKSlot)
admin.site.register(AK, AKAdmin)
admin.site.register(RoomAssignment)
admin.site.register(News)