from .models import Person
from django.forms import ModelForm

class NewUserForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'alias']
