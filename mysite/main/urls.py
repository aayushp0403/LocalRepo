from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('codeforces/', views.codeforces_stats, name='codeforces'),
]
