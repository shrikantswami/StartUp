from django.urls import path
from age_calculator import views

urlpatterns = [
    path("", views.calculator_view, name='calculator_view')
]