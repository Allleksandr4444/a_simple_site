from .models import Table
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, Textarea

class TableForm(ModelForm):
   class Meta:
       model =Table
       fields = ['title', 'text']
       widgets = {
           'title': TextInput(attrs={"class": "form_control", "placeholder": "Введите название"}),
           'text': Textarea(attrs={"class": "form_control", "placeholder": "Введите описание"})
       }