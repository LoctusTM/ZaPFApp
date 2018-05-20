from django.db import models

class Timeslot(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    name = models.CharField(max_length=200, blank=True)
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
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Zeitslots"
        verbose_name = "Zeitslot"

class Room(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Räume"
        verbose_name = "Raum"

class AKSlot(Timeslot):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "AK-Slots"
        verbose_name = "AK-Slot"

class AK(models.Model):
    akslot = models.ForeignKey(AKSlot, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    responsible = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "AKs"
        verbose_name = "AK"

class RoomAssignment(models.Model):
    room = models.ForeignKey(Room, related_name='zuordnung', on_delete=models.CASCADE)
    group = models.ForeignKey(AK, related_name='zuordnung', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Raumzuordnungen"
        verbose_name = "Raumzuordnung"


class News(models.Model):
    message = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.message

    class Meta:
        verbose_name_plural = "Nachrichten"
        verbose_name = "Nachricht"


