from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from api import views

routers = DefaultRouter()
routers.register('studapi/', views.ModelViewStudent, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
