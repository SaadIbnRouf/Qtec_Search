from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Search
from .models import SearchHistory

# Create your views here


def index(request):
    search = Search()
    if request.method == 'POST':
        search = Search(request.POST)
        if search.is_valid():
            search.save()
        return redirect('/')

    return render(request, 'SearchHistory/index.html')


def search_details(request):
    lists = SearchHistory.objects.all()
    lists_keyword = SearchHistory.objects.values('keyword').distinct()
    lists_user = SearchHistory.objects.select_related('user')
    context = {'lists': lists, 'lists_keyword': lists_keyword, 'lists_user': lists_user}

    return render(request, 'SearchHistory/search_details.html', context)

# <input type="checkbox" name="is_closed" value="closed">
# <input type="checkbox" name="is_closed" value="closed" {% if 'closed' in 'is_closed %} checked {% else %} '' {% endif %}>




