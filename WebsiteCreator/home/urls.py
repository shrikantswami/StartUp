from django.urls import path
from home import views


urlpatterns = [
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact')
]
