from django.urls import path
from rango import views

app_name = 'rango'

# Put paths for /rango/<url> here
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
