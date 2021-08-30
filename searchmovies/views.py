from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
import requests


# Create your views here.
def indexview(request):
    if request.method == 'GET':
        # search = request.GET.get('search')
        # return redirect('searchapp:search')
        pass
    context = {}
    return render(request, 'index.html', context)


def searchview(request):
    # search_item = request.GET.get('search')
    if request.method == 'GET':
        search_item = request.GET.get('search')

        url = 'https://api.themoviedb.org/3/search/multi?api_key='
        key = '22291a63e8620e89def2060f81a42da5'
        response = requests.get(f'{url}{key}&query={search_item}').json()

        context = {
            'search_item': search_item,
            'response': response,
        }
    return render(request, 'search-result.html', context)
