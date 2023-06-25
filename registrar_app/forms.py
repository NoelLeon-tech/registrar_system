from django import forms
from .models import *
from datetime import datetime

class QueueForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        # self.instance works here
        if status == "Processed":
            cleaned_data["time_finished"] = datetime.now().time()
        return cleaned_data