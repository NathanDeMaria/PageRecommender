from django.conf.urls import url

from . import views


urlpatterns = [
    url('^add$', views.add, name='add'),
    url('^load$', views.load, name='load')
]
