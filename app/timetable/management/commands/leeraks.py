import numpy as np
import random
import operator

from django.core.management.base import BaseCommand
from timetable.models import Timeslot, Room, AKSlot, AK, RoomAssignment, News
from constance import config


class Command(BaseCommand):    
    def add_arguments(self, parser):
        parser.add_argument('leeraks', type=int, nargs='?', default=1)


    def _add_leeraks(self, n):
        for i in range(n):
            ak = AK(short="-", name="-")
            ak.save()

    def handle(self, *args, **options):
        n = options.get('leeraks', None)
        self._add_leeraks(n)