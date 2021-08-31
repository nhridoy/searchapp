from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from searchmovies.models import SearchHistory
import requests
from datetime import date
import datetime
from django.utils import timezone


# Create your views here.
def indexView(request):
    context = {}
    return render(request, 'index.html', context)


@login_required
def searchView(request):
    # search_item = request.GET.get('search')
    if request.method == 'GET':
        search_item = request.GET.get('search')

        url = 'https://api.themoviedb.org/3/search/multi?api_key='
        key = '22291a63e8620e89def2060f81a42da5'
        response = requests.get(f'{url}{key}&query={search_item}').json()

        search_history = SearchHistory.objects.create(user=request.user, search_keyword=search_item,
                                                      search_results=int(response['total_results']))

        context = {
            'search_item': search_item,
            'response': response,
        }
    return render(request, 'search-result.html', context)


@login_required
def searchHistoryView(request):
    search_history = SearchHistory.objects.filter(user=request.user).order_by('-search_date')
    context = {
        'search_history': search_history,
    }
    return render(request, 'search-history.html', context)


# Filter Data
@login_required
def filter_data(request):
    today = request.GET.getlist('today[]')
    yesterday = request.GET.getlist('yesterday[]')
    all_data = request.GET.getlist('all[]')

    allSearchResults = SearchHistory.objects.filter(user=request.user).order_by('-search_date').distinct()
    if request.method == 'POST':
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        allSearchResults = allSearchResults.filter(
            search_date__range=(startDate, endDate)).values(
            'search_keyword',
            'search_results',
            'search_date')
        return JsonResponse({'data': list(allSearchResults)})

    allSearchResults = SearchHistory.objects.filter(user=request.user).order_by('-search_date').values(
        'search_keyword',
        'search_results',
        'search_date')

    if len(today) > 0:
        allSearchResults = allSearchResults.filter(search_date__day=date.today().day,
                                                   search_date__month=date.today().month,
                                                   search_date__year=date.today().year).values('search_keyword',
                                                                                               'search_results',
                                                                                               'search_date')

    elif len(yesterday) > 0:
        allSearchResults = allSearchResults.filter(
            search_date__day=(date.today() - datetime.timedelta(days=1)).strftime('%d'),
            search_date__month=(date.today() - datetime.timedelta(days=1)).strftime('%m'),
            search_date__year=(date.today() - datetime.timedelta(days=1)).strftime('%Y')).values('search_keyword',
                                                                                                 'search_results',
                                                                                                 'search_date')
    elif len(all_data) > 0:
        allSearchResults = SearchHistory.objects.filter(user=request.user).order_by('-search_date').values(
            'search_keyword',
            'search_results',
            'search_date')

    return JsonResponse({'data': list(allSearchResults)})
