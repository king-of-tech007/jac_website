from django.urls import path, include

from .views import homepage , aboutpage , activitypage , gallerypage , jkapage , activitydetailspage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage, name="home page"),
    path('about/', aboutpage, name="about page"),
    path('activity/', activitypage, name="activity page"),
    path('activity-details/', activitydetailspage, name="activity details page"),
    path('gallery/', gallerypage, name="gallery page"),
    path('jka/', jkapage, name="jka page"),
    path('login/', include("account_management.urls")),
    path('blog/', include('blog_management.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
