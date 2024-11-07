from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'main/index_file.html')


def aboutpage(request):
    return render(request, 'main/about_file.html')


def activitypage(request):
    return render(request, 'main/activity_file.html')


def activitydetailspage(request):
    return render(request, 'main/activity_details_file.html')


def gallerypage(request):
    return render(request, 'main/gallery_file.html')


def jkapage(request):
    return render(request, 'main/jka_page_file.html')




