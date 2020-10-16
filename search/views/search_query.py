import simplejson as json

# Django Module
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Thirdparty Module
from haystack.query import SearchQuerySet

@csrf_exempt
def SearchQueryView(request):
    query_text = request.GET.get('q', '')
    if query_text == '':
        return redirect('home')
    else:
        courses = SearchQuerySet().filter(
            content_auto=query_text)
        return render(request,'search/search.html', {'courses': courses})