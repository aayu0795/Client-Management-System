import io
import csv
from django import forms
from .models import Customer, CustomUser, CsvFile
from django.utils.translation import ugettext_lazy as _


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['agent', 'name', 'age', 'gender', 'contact']
        widgets = {'agent': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['age'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact'].widget.attrs.update(
            {'class': 'form-control', 'minLength': 10, 'maxLength': 10})


class SingleCustomerDataForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['agent', 'name', 'age', 'gender', 'contact']
        widgets = {'agent': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['age'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact'].widget.attrs.update(
            {'class': 'form-control', 'onkeyup': 'validnumber(this)'})


class BatchCustomersDataForm(forms.Form):
    agent_id = forms.IntegerField(widget=forms.HiddenInput())
    data_file = forms.FileField(label=_('Data File'))

    def clean_data_file(self):
        f = self.cleaned_data['data_file']

        if f:
            ext = f.name.split('.')[-1]
            if ext != 'csv':
                raise forms.ValidationError('File type not supported')
        return f

    def process_data(self):
        # CsvFile.objects.create(
        #     agent_id=self.cleaned_data['agent_id'],
        #     csv_file=self.cleaned_data['data_file'],
        # )
        agent_id = self.cleaned_data['agent_id']
        f = io.TextIOWrapper(self.cleaned_data['data_file'].file)
        reader = csv.DictReader(f)

        for customer in reader:
            Customer.objects.create(agent=CustomUser.objects.get(id=agent_id),
                                    name=customer['name'],
                                    age=customer['age'],
                                    gender=customer['gender'],
                                    contact=customer['contact']
                                    )
