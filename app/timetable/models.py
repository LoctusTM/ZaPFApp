from django.db import models

class Timeslot(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    start = models.DateTimeField('start')
    end = models.DateTimeField('end')
    event_type = (
        ('food', 'food'),
        ('plenum', 'plenum'),
        ('ak', 'ak'),
        ('social', 'social'),
        ('else', 'else')
    )
    event_type = models.CharField(max_length=10, choices=event_type, default='ELSE')

class Room(models.Model):
	name = models.CharField(max_length=200)

class AKSlot(Timeslot):
    pass

class AK(models.Model):
    akslot = models.ForeignKey(AKSlot, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    responsible = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

class RoomAssignment(models.Model):
    room = models.ForeignKey(Room, related_name='zuordnung', on_delete=models.CASCADE)
    group = models.ForeignKey(AK, related_name='zuordnung', on_delete=models.CASCADE)