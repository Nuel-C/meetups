from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'),
    path('meetups/<meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('meetups/<meetup_slug>', views.meetup_details, name='meetup-detail')
]