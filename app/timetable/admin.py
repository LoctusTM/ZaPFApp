from django.contrib import admin

from .models import Timeslot, Room, AKSlot, AK, RoomAssignment, News

class AKAdmin(admin.ModelAdmin):
    list_display = ('name', 'short', 'akslot', 'room', 'responsible', 'backup', 'public_id', 'published', 'kleine_fachschaften')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('time', 'message')


admin.site.register(Timeslot)
admin.site.register(Room)
admin.site.register(AKSlot)
admin.site.register(AK, AKAdmin)
admin.site.register(RoomAssignment)
admin.site.register(News, NewsAdmin)
