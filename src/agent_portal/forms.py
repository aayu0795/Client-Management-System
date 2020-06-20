import io
import csv
from django import forms
from .models import Customer


class BatchdataForm(forms.Form):
    agent_id = forms.IntegerField()
    data_file = forms.FileField()

    def clean_data_file(self):
        f = self.cleaned_data['data_file']

        if f:
            ext = f.name.split('.')[-1]
            if ext != 'csv':
                raise forms.ValidationError('File type not supported')
        return f

    def process_data(self):
        agent_id = self.cleaned_data['agent_id']
        f = io.TextIOWrapper(self.cleaned_data['data_file'].file)
        reader = csv.DictReader(f)

        for customer in reader:
            # Customer.objects.create(
            print(agent_id, customer['name'], customer['age'],
                  customer['gender'], customer['contact'])
