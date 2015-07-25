from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    if 'good.x' in request.POST:
        print "Good"
    elif 'bad.x' in request.POST:
        print "Bad"
    else:
        raise ValueError("Unrecognized response")

    return render(request, "rated.html")