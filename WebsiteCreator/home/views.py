"""
This is home screen page
"""
from django.shortcuts import render

# Create your views here.


def home(request):
    """
    This is Home Page
    """
    # hp_link_context = get_home_page_links(request)
    return render(request, "home.html", {})