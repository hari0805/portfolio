from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import FileResponse
from firstapp.models import Aboutmodel

class Homeview(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,*args, **kwargs):
        context = super(Homeview, self).get_context_data(*args,**kwargs)
        context['aboutme'] = Aboutmodel.aboutme.last()
        return context


class Download_Resume(TemplateView):
    
    def get(self,*args, **kwargs):
        file = Aboutmodel.aboutme.last()
        response = FileResponse(file.Resume, content_type='application/pdf')
        response['Content-Disposition'] = 'filename=file.Resume'
        return response