from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', BookQueryListView.as_view(), name=''),
    path('booksearch/', Book_Search.as_view(), name=''),
    path('booksingle/<int:pk>/', Book_Single.as_view(), name=''),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)