from django.urls import path
from home import views


urlpatterns = [
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("privacy-policy", views.privacy_policy, name='privacy-policy'),
    path("terms", views.terms, name='terms')
]
