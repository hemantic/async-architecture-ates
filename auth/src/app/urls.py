from app import views
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = []

urlpatterns = [
    path('', views.index, name='index'),
]

# Django admin
urlpatterns += [
    path('admin/', admin.site.urls),
]

# Django healthchecks
urlpatterns += [
    path('api/v1/healthchecks/', include('django_healthchecks.urls')),
]
