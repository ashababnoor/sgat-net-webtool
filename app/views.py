from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
import base64

class HomeView(View):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class HandleFiles(View):
    template_name = 'upload.html'
    def post(self, request, *args, **kwargs):
        image = request.FILES['file']
        path = default_storage.save(image.name, ContentFile(image.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        with open(tmp_file, 'rb') as f:
           file_data = base64.b64encode(f.read()).decode('utf-8')

        response = HttpResponse(file_data)
        response['Content-Type'] = 'image/jpeg'
        response['Content-Disposition'] = f'attachment; filename="{ image.name }"'
        
        return response