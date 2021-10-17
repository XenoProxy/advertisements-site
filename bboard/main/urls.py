from django.urls import path
from django.contrib import admin

from .views import index, other_page


app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),  # must be first
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
