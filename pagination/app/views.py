from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from app.settings import BUS_STATION_CSV
import csv


all_stations = []
with open(BUS_STATION_CSV, 'r', encoding='cp1251') as f:
    reader = csv.DictReader(f, delimiter=',')
    for line in reader:
        all_stations.append({
            'Name': line['Name'],
            'Street': line['Street'],
            'District': line['District']
        })


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = request.GET.get('page')
    if not current_page or not current_page.isdigit():
        current_page = 1
    else:
        current_page = int(current_page)

    start = (current_page - 1) * 10
    finish = start + 10
    if finish > len(all_stations):
        finish = len(all_stations)

    bus_stations = all_stations[start:finish]

    if current_page > 1:
        prev_page_url = f'?page={current_page - 1}'
    else:
        prev_page_url = None

    if len(all_stations) <= current_page * 10:
        next_page_url = None
    else:
        next_page_url = f'?page={current_page + 1}'

    return render_to_response('index.html', context={
        'bus_stations': bus_stations,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url
    })
