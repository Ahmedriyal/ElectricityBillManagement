from django import forms

from .models import occupants, floors, locations

# ------ Occupants Form ------
class OccupantsForm(forms.ModelForm):
    class Meta:
        model = occupants
        fields = '__all__'
        exclude = ('status',)
        widgets = {
            'start_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}
            ),
            'end_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}
            )
        }

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