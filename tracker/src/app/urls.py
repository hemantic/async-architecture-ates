from app import views
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = []

urlpatterns += [
    path('', views.index, name='index'),
]

# Auth
urlpatterns += [
    path('', include('social_django.urls', namespace='social'))
]

# Django admin
urlpatterns += [
    path('admin/', admin.site.urls),
]

# Django healthchecks
urlpatterns += [
    path('api/v1/healthchecks/', include('django_healthchecks.urls')),
]
