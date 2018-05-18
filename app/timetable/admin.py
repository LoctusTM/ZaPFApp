from django.contrib import admin

from .models import Timeslot, Room, AKSlot, AK, RoomAssignment

admin.site.register(Timeslot)
admin.site.register(Room)
admin.site.register(AKSlot)
admin.site.register(AK)
admin.site.register(RoomAssignment)