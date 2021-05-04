from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomePage(TemplateView):
    template_name = 'main.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context