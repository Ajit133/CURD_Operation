from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm
from tasks.models import Student


class StudentForm(forms.ModelForm):
    Birth_Date = forms.DateField(widget=forms.TextInput(attrs={"type":"date"}))
    class Meta:
        model = Student
        fields = "__all__"

