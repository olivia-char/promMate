from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^homePage$', views.homePage),
    url(r'^cart$', views.cart),
    url(r'^userPage$', views.userPage),
    url(r'^match$', views.match),
    url(r'^addDress$', views.addDress),
]