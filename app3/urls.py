from django.urls import path
app_name='rcb'
from app3.views import rcb
urlpatterns=[
    path('rcb/',rcb,name='rcb')
]