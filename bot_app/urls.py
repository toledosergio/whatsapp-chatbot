from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns = [
    path('', include('bot_app.urls')),
    path('admin/', admin.site.urls),
]
