from django.http import HttpResponse
from django.shortcuts import render
from oauth2_provider.decorators import protected_resource


def index(request):
    return render(request, 'index.html')


@protected_resource()
def profile(request):
    return HttpResponse({'username': request.user.username, 'email': request.user.email}, content_type='application/json')
