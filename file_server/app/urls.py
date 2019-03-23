from django.urls import path, re_path

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from app.views import FileList, file_content

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.FileList и .views.file_content
    # path(..., name='file_list'),
    # path(..., name='file_list'),
    # path(..., name='file_content'),

    path('', FileList.as_view(), name='file_list'),
    re_path(r'(?P<date>([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])))', FileList.as_view(), name='file_list'),
    path('<str:name>', file_content, name='file_content')
]
