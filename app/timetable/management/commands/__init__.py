from django.core.management.base import BaseCommand
from timetable.models import Timeslot, Room, AKSlot, AK, RoomAssignment, News

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = ''

    def _create_tags(self):
        tlisp = AK(name='Lisp')
        tlisp.save()

        tjava = Tag(name='Java')
        tjava.save()

    def handle(self, *args, **options):
        self._create_tags()