from django.shortcuts import render

# Create your views here.
def introduce(request, username):
    return render(request, 'introduce.html', {'username': username}) 