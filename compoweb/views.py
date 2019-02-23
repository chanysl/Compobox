from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'compoweb/post_list.html', {})

def index(request):
    return render(request, 'compoweb/index.html', {})