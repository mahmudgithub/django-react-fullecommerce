from django.shortcuts import render
from django.views.generic import TemplateView

# def one(request):
#     return render(request,'home.html')

class one(TemplateView):
    template_name='home.html'
