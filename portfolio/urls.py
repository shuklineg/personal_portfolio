from django.urls.conf import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home')
]
