from django.urls import path
from search.views.search_query import SearchQueryView
from search.views.search_autocomplete import SearchQueryAutocomplete

app_name = 'search'

urlpatterns = [
    path('', SearchQueryView, name='search'),
    path('autocomplete/', SearchQueryAutocomplete, name='searchauto')
]