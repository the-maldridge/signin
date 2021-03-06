from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='board'),
    url(r'^tap-in/([\d]*)$', views.tap_in),
    url(r'^tap-out/([\d]*)$', views.tap_out),
    url(r'^tap-all-out$', views.tap_all_out),
    url(r'^log$', views.log),
    url(r'^new$', views.new),
]
