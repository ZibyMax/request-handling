from datetime import datetime, date
import os

from django.shortcuts import render
from django.views.generic import TemplateView

from app.settings import FILES_PATH


class FileList(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, date=None):
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        files_list = os.listdir(FILES_PATH)
        files = []
        for file in files_list:
            files.append({
                'name': file,
                'ctime': datetime.fromtimestamp(os.path.getctime(os.path.join(FILES_PATH, file))).date(),
                'mtime': datetime.fromtimestamp(os.path.getmtime(os.path.join(FILES_PATH, file))).date()
            })

        if date:
            date = datetime.strptime(date, '%Y-%m-%d').date()

        return {
            'files': files,
            'date': date  # Этот параметр необязательный
            # 'files': [
            #    {'name': 'file_name_1.txt',
            #     'ctime': datetime.datetime(2018, 1, 1),
            #     'mtime': datetime.datetime(2018, 1, 2)}
            #],
            # 'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
        }


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_name = name
    with open(os.path.join(FILES_PATH, file_name)) as f:
        file_content = f.read()

    return render(
        request,
        'file_content.html',
        context={'file_name': file_name,
                 'file_content': file_content}
    )

