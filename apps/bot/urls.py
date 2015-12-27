from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import update, insert, ping

urlpatterns = [
    url(r'^update/', login_required(update), name='update'),
    url(r'^insert/', login_required(insert), name='insert'),
    url(r'^ping/', login_required(ping), name='ping'),
]

