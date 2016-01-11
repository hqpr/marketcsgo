from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.account.views import login_view, logout_view, SettingsView, switch

urlpatterns = [
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),

    url(r'^settings/$', login_required(SettingsView.as_view()), name="settings"),
    url(r'^switch/$', login_required(switch), name="switch"),

]

