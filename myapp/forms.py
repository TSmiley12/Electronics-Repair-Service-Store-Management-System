from django import forms
from .models import Problems_section

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problems_section
        fields = ['title', 'desc',]  # Adjust fields as needed
