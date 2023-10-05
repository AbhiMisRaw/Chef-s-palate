
from django.contrib import admin
from django.urls import include, path
from food import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/',include('food.urls')),
]
