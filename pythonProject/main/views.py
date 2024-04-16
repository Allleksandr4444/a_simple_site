from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Table
from .forms import TableForm

def text(request):
   table=Table.objects.all()
   return render(request, "main/text.html", {'table':table})

def text2(request):
   erorr = ''
   if request.method == 'POST':
      form = TableForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('/')
      else:
         erorr = 'Форма заполнена неверно'
   form = TableForm()
   context={'form':form, "erorr":erorr}

   return render(request, "main/text2.html",context)




