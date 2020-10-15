from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
import logging


def HomeView(request):
    # Translation
    # from django.utils import translation
    # user_language = 'de'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #     del resquest.session[translation.LANGUAGE_SESSION_KEY]
    ##############################
    title = _('Home')
    context = {
        'title': title
    }
    return render(request, 'home.html', context)