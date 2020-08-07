from django.urls import path
from . import views

urlpatterns = [
    path('', views.link_in, name='link_in'),

]
