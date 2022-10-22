from telnetlib import STATUS
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
import base64
from .models import *

class HomeView(View):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class HandleFiles(View):
    template_name = 'upload.html'
    def post(self, request, *args, **kwargs):
        image = request.FILES['file']
        img_obj = Image.objects.create(**{ 'image' : image })
        return JsonResponse({ 'id' : img_obj.id })

class ProceedPromtView(View):
    template_name = 'proceed.html'
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        img_obj = Image.objects.get(pk=id)
        return render(request, template_name=self.template_name, context={'image' : img_obj})