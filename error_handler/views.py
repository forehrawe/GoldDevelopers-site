from django.shortcuts import render

# Create your views here.
class custom_404:
    def get(request):
        return render(request, '404.html', status=404)