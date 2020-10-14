from django.shortcuts import render
from django.views.generic import TemplateView
import os

class SampleTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ENV"] = os.environ['ENV']
        return context
# Create your views here.
