from django.urls import path
from .views import RegisterAPI,WorksAPI

urlpatterns=[
    path('register/',RegisterAPI.as_view()),
    path('works/',WorksAPI.as_view()),
]