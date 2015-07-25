from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from extension.models import Article
from datetime import datetime


@require_http_methods(['POST'])
@csrf_exempt
def add(request):

    if 'good.x' in request.POST:
        response = 'L'
    elif 'bad.x' in request.POST:
        response = 'D'
    else:
        raise ValueError("Unrecognized response")

    a = Article(url=request.POST['url'], access_time=datetime.now(), response=response)
    a.save()

    return render(request, "rated.html")