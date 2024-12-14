from django.urls import path
from age_calculator import views

urlpatterns = [
    path("/age-calculator", views.calculator_view, name='calculator_view'),
    path("/percentage-calculator", views.percentage_calculator, name='percentage_calculator')
]