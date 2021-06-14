from django.urls.conf import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:id>/', views.detail, name='detail'),
]
