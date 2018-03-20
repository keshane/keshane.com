from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'keshane_site/index.html')


def contact(request):
    return render(request, 'keshane_site/contact.html')
