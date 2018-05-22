import numpy as np
import random
import operator

from django.core.management.base import BaseCommand
from timetable.models import Timeslot, Room, AKSlot, AK, RoomAssignment, News
from constance import config


def n_t(n, k):
    return (n%k, n//k)

def t_n(x1, x2, k):
    return x1 + x2* k

def wh(array, val):
    return np.argwhere(array==val)[0][0], np.argwhere(array==val)[0][1]


Räume = config.rooms
Zeitslots = config.timeslots


"""
aks = np.arange(1, AKs+1).astype(int)
raum_zeit = np.zeros((Zeitslots, Räume)) # 8 Räume, 7 Zeitslots
raum_zeit.astype(int)

aks2 = aks.copy()
aks2 = np.append(aks2, np.zeros(Räume*Zeitslots-AKs))

results = []

for k in range(100):
    random.shuffle(aks2)
    
    for i, ak in enumerate(aks2):
        raum_zeit[n_t(i, Zeitslots)[0]][n_t(i, Zeitslots)[1]] = ak
    
    kleine_fachschaften = np.zeros((Zeitslots, Räume))
    
    for x, y in [(x, 1) for x in kleine_fachschaften_aks]:
        kleine_fachschaften[wh(raum_zeit, x)] = y
        
    badness = len((np.argwhere(np.count_nonzero(kleine_fachschaften, 1)>1)))
    
    results.append((badness, raum_zeit, kleine_fachschaften))
"""

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = ''

    def _timeslot_assignment(self):
        r = Room.objects.filter(hörsaal=False)
        a = AK.objects.filter(backup=False)
        s = AKSlot.objects.filter(backup=False)

        print(r)


        Räume = len(r)
        Zeitslots = len(s)

        kleine_fachschaften_aks = [(i, ak.kleine_fachschaften) for i, ak in enumerate(a)]

        aks = np.arange(1, len(a)+1).astype(int)
        raum_zeit = np.zeros((Zeitslots, Räume)) # 8 Räume, 7 Zeitslots
        raum_zeit.astype(int)

        aks2 = aks.copy()
        aks2 = np.append(aks2, np.zeros(Räume*Zeitslots-len(a)))

        results = []

        for k in range(100):
            random.shuffle(aks2)
            
            for i, ak in enumerate(aks2):
                raum_zeit[n_t(i, Zeitslots)[0]][n_t(i, Zeitslots)[1]] = ak
            
            kleine_fachschaften = np.zeros((Zeitslots, Räume))
            
            for x, y in kleine_fachschaften_aks:
                kleine_fachschaften[wh(raum_zeit, x)] = y
                
            badness = len((np.argwhere(np.count_nonzero(kleine_fachschaften, 1)>1)))
            
            results.append((badness, raum_zeit, kleine_fachschaften))

        for i, slot in enumerate(results[0][1]):
            for j, ak in enumerate(slot):
                print(i, j, int(ak))
                print(j)
                if int(ak) != 0:
                    ak_elem = a[int(ak)-1]
                    ak_elem.room = r[j]
                    ak_elem.akslot = s[i]
                    ak_elem.save()
    def handle(self, *args, **options):
        self._timeslot_assignment()