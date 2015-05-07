from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/', views.create, name='create'),
    url(R'^edit/(?P<task_id>[0-9]+)/', views.edit, name='edit'),
    url(r'^imprint/', views.imprint, name='imprint'),
]
