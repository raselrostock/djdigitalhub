import simplejson as json

# Django Module
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Thirdparty Module
from haystack.query import SearchQuerySet

def SearchQueryAutocomplete(request):
    sqs = SearchQuerySet().autocomplete(
        content_auto=request.GET.get('q', ''))
    suggestions = [result.title for result in sqs]
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')