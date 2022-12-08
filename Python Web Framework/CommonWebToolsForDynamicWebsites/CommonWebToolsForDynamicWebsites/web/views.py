import random
from time import sleep

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


def very_slow_operation():
    sleep(30)
    return random.randint(1, 520)


@cache_page(1 * 60)
def index(request):
    value = very_slow_operation()
    return HttpResponse(f'Value is {value}')


def session_view(request):
    clicks_count = request.session.get('CLICK_COUNT', 0) + 1
    request.session['CLICK_COUNT'] = clicks_count
    return HttpResponse(f'clicks: {clicks_count}')


