from django import forms

class ChangeForm(forms.Form):
    slot_1 = forms.IntegerField(label='Slot 1')
    slot_2 = forms.IntegerField(label='Slot 2')
