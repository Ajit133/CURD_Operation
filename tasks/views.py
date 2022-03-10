from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
import re
from django.shortcuts import render
from tasks import forms
from tasks.models import Student
from tasks.forms import StudentForm

# Create your views here.

def index(request):
    student_infoo = Student.objects.all()
    dict = {"title":"Home Page","student_infoo":student_infoo}
    return render(request,'task/index.html',context=dict)
def student_form(request):
    new_form = forms.StudentForm()

    if request.method == "POST":
        new_form = forms.StudentForm(request.POST)
        if new_form.is_valid():
            new_form.save(commit=True)
            return redirect('home')
    dict = {'title':"Student Form",'new_form':new_form}
    return render(request,'task/student_form.html',context=dict)

def Student_Information(request,pk):
    # s_id = Student.objects.get(pk=s_id)
    s_id = get_object_or_404(Student,pk=pk)
    dict = {'title':'Student_information',"s_id":s_id}
    return render(request,'task/student_info.html',context= dict)

def Student_Edit(request,pk):
    student = get_object_or_404(Student,pk=pk)
    S_Form = StudentForm(instance=student)

    if request.method == "POST":
         s_form = StudentForm(request.POST,instance=student)
         if s_form.is_valid():
             s_form.save()
             return redirect('home')
    return render(request,'task/edit_s.html',context={"S_Form":S_Form})
def Student_Delete(request,pk):
    student_delete = get_object_or_404(Student,pk=pk)
    student_delete.delete()
    return redirect('home')