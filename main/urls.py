from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('contact', views.contact, name="contact")
]
