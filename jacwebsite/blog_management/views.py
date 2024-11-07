from django.shortcuts import render

# Create your views here.
def homepage_blog(request):
    return render(request, "blog_management/index.html")
