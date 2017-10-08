from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse('Hello World')


def json(request):
    return JsonResponse({'hello': 'world'})
