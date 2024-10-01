from django.urls import path
from . import views

#URL config - url name, which to be triggered
urlpatterns = [
    path("", views.index), # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]