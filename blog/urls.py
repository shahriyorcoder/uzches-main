from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('',NewsQueryListView.as_view(), name=''),
    path('news_search/', News_Search.as_view(), name=''),
    path('course_list/', CourseListView.as_view(), name=''),
    path('news_single/<int:pk>/', News_Single.as_view(), name=''),
    path('course_single/<int:pk>/', CourseDetailView.as_view(), name=''),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)