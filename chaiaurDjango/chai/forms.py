from django import forms
from .models import ChaiVarietie

class ChaiVarietieForm(forms.Form):
    chai_varieties = forms.ModelChoiceField(
        queryset=ChaiVarietie.objects.all(), # pylint: disable=no-member
        label="Select Chai Varieties",
        widget=forms.Select(attrs={
            'class': 'border border-gray-300 rounded px-3 py-2 w-full text-gray-700',
        })
    )