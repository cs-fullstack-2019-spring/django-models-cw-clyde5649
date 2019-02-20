from django.http import HttpResponse


def index(request):
    return HttpResponse("this is about most dogs.")

def dog(request):
    return HttpResponse("")

def breed(request):
    return HttpResponse(" ")

def color(request):
    return HttpResponse(" ")

def gender(request):
    return HttpResponse(" ")



