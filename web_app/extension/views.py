from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from extension.models import Article
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re
from unidecode import unidecode
import string
from django.http import JsonResponse, HttpResponse
import tfidf


@require_http_methods(['POST'])
@csrf_exempt
def add(request):

    if 'good.x' in request.POST:
        response = 'L'
    elif 'bad.x' in request.POST:
        response = 'D'
    else:
        raise ValueError("Unrecognized response")

    url = request.POST['url']
    arts = Article.objects.all()
    url_list = []
    for article in arts:
        url_list.append(article.url)

    # New URL
    if url not in url_list:
        new_text = get_html_text(url)

        _ = Article.objects.create(url=request.POST['url'], body_text=new_text,
                                   access_time=datetime.utcnow(), response=response)
        return render(request, "rated.html")
    # Same url but changed response
    elif url in url_list and Article.objects.get(url=url).response != response:
        tmp_art = Article.objects.get(url=url)
        tmp_art.response = response
        tmp_art.save()
        return render(request, "rate_updated.html")
    # Already rated
    else:
        return render(request, "already_rated.html")


@require_http_methods(['POST'])
@csrf_exempt
def load(request):

    url = request.POST['url']
    arts = Article.objects.all()
    if len(arts) == 0:
        content = "Like pages to get started!"
    else:
        bodies_like = ''
        bodies_dislike = ''
        # Grab likes and dislikes
        for article in arts:
            if article.response == 'L':
                bodies_like += ' '
                bodies_like += str((unidecode(article.body_text)))
            elif article.response == 'D':
                bodies_dislike += ' '
                bodies_dislike += str(unidecode(article.body_text))
            else:
                raise ValueError('Unknown rating encountered. Contact admin to reset database.')
        bodies_like_words = bodies_like.split()
        bodies_dislike_words = bodies_dislike.split()
        table = tfidf.tfidf()
        table.addDocument('likes', bodies_like_words)
        table.addDocument('dislikes', bodies_dislike_words)
        compare_text = get_html_text(url)
        comparisons = table.similarities(compare_text)
        print comparisons, '\n'
        if comparisons[0][1] > comparisons[1][1]:
            content = 'LIKE ({0}% Certain)'.format(round(100. * comparisons[0][1], 2))
        elif comparisons[0][1] < comparisons[1][1]:
            content = 'DISLIKE ({0}% Certain)'.format(round(100. * comparisons[1][1], 2))
        elif comparisons[0][1] == comparisons[1][1]:
            content = 'NEUTRAL ({0}% Certain)'.format(round(100. * comparisons[0][1], 2))
        else:
            raise ValueError('You should never receive this error. If so please send the admin a message saying so...')

    response = HttpResponse(content_type='text/plain')
    response.write(str(content))
    return response


# Helper function used to cut down HTML text to readable portions
def get_html_text(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    texts = soup.findAll(text=True)
    visible_texts = filter(visible, texts)
    new_vis_text = filter(lambda x: not(x.isspace()) and (x[0] not in string.punctuation) and
                                    not(x.isdigit()) and (x[0].isalnum()), visible_texts)
    return " ".join(new_vis_text)

# Helper function used to determine visible section of HTML text
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match("<!--.*-->", str(unidecode(element))):
        return False
    return True