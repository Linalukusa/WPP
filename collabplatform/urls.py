
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', include('authentication.urls')),
    path('', include('projects.urls')),
    path('', include('event.urls')),
    path('', include('discussion.urls')),
    path('', include('research.urls')),
    path('', include('homepage.urls')),
    path('', include('friends.urls')),
    path('', include('practitionners.urls')),
    path('', include('report.urls')),
    path('',include('forum.urls')),
    path('',include('comments.urls')),
    path('',include('organisation.urls')),



    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
