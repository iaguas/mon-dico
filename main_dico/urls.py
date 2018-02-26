from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dictionary', views.dictionary),
    path('new-word', views.new_word),
    path('report', views.report)
]
