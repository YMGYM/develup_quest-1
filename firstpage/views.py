from django.shortcuts import render

def splash(request):
    return render(request, 'splash.html')


def frontpage(request):
    return render(request, 'frontpage.html')