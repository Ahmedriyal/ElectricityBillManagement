from django import forms

from .models import occupants, floors, locations

# ------ Occupants Form ------
class OccupantsForm(forms.ModelForm):
    class Meta:
        model = occupants
        fields = '__all__'

# ------ Floors Form ------
class FloorsForm(forms.ModelForm):
    class Meta:
        model = floors
        fields = '__all__'

# ------ Floor Unit Form ------
class UnitForm(forms.ModelForm):
    class Meta:
        model = locations
        fields = '__all__'