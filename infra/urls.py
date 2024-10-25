
# == This code was created by https://noauto-nolife.com/post/django-auto-create-urls/ == #

from django.urls import path
from . import views

app_name    = "infra"
urlpatterns = [
    path("", views.index, name="index"),
]
