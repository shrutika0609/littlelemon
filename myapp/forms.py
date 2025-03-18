from django.forms import ModelForm
from .models import Logger

class LogForm(ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'  # Include all fields from the model