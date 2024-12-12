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


def about(request):
    """
    This is Home Page
    """
    return render(request, "about.html", {})


def contact(request):
    """
    This is Home Page
    """
    context = {}
    if request.method == "POST":
        print(" method is POST")
        context = {'name': request.POST['name'], 'email': request.POST['email'], 'message': request.POST['message']}
        print(context)
    return render(request, "contact.html", context)


def privacy_policy(request):
    """
    This is Home Page
    """
    return render(request, "privacy-policy.html", {})


def terms(request):
    """
    This is Home Page
    """
    return render(request, "terms.html", {})
