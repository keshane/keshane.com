from django.shortcuts import render


def index(request):
    """Renders the home (index) page of the site"""
    return render(request, 'keshane_site/index.html')


def contact(request):
    """Renders the contact page"""
    return render(request, 'keshane_site/contact.html')
