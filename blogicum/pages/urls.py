from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('rules/', views.rules, name='about'),
    path('about/', views.about, name='rules'),
]
