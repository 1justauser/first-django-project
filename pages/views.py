from django.http import HttpResponse


def HomePageView(request):
    return HttpResponse('Its my first Django Project!')