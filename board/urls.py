from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^tap-in/([\d]*)$', views.tap_in),
    url(r'^tap-out/([\d]*)$', views.tap_out),
]
