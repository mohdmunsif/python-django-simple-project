from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'entries'

urlpatterns = [
    path("", views.index, name="index"),
    path("submit", views.submit, name="submit"),
    path("welcome", views.welcome, name="welcome"),
    path("entry/<int:entry_id>", views.oneentry, name="oneentry"),
    path("browse", views.browse, name="browse"),
    path("search", views.search, name="search"),
    path("searchage", views.searchage, name="searchage")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
