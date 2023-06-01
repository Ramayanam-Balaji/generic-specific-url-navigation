from django.urls import path
app_name='csk'
from app2.views import csk
urlpatterns=[
    path('csk/',csk,name='csk')
]
