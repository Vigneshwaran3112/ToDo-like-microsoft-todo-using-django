
from django.contrib import admin
from django.urls import path, include
from app1 import views, urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls))
]
