from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^signin$', views.signin),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^signup$', views.signup),
    url(r'^dashboard$', views.dashboard),
    url(r'^user/add$', views.addUser),
    url(r'^add$', views.add),
    url(r'^save/(?P<id>\d+)$', views.save),
    url(r'^user/edit$', views.edit),
    url(r'^user/delete/(?P<id>\d+)$', views.delete),
    url(r'^admin_edit/(?P<id>\d+)$', views.adminEdit),
    url(r'^logoff$', views.logoff),
]
