from datetime import datetime, date
import os

from django.shortcuts import render
from django.views.generic import TemplateView

#from app.settings import FILES_PATH
from django.conf import settings


class FileList(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, date=None):
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        files_list = os.listdir(settings.FILES_PATH)
        files = []

        if date:
            date = datetime.strptime(date, '%Y-%m-%d').date()

        for file in files_list:
            ctime = datetime.fromtimestamp(os.path.getctime(os.path.join(settings.FILES_PATH, file)))
            mtime = datetime.fromtimestamp(os.path.getmtime(os.path.join(settings.FILES_PATH, file)))
            if not date or date == ctime.date() or date == mtime.date():
                files.append({
                    'name': file,
                    'ctime': ctime,
                    'mtime': mtime
                })

        return {
            'files': files,
            'date': date
        }


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_path = os.path.join(settings.FILES_PATH, name)
    content = ''
    if os.path.isfile(file_path):
        with open(os.path.join(settings.FILES_PATH, name)) as f:
            content = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name,
                 'file_content': content}
    )
