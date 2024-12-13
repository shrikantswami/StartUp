from django.urls import path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from home import views


urlpatterns = [
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("privacy-policy", views.privacy_policy, name='privacy-policy'),
    path("terms", views.terms, name='terms'),
    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml"))
]
