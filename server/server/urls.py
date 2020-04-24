from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('scores/', include('scores.urls'), name='scores'),
    path('admin/', admin.site.urls, name='admin'),
]
