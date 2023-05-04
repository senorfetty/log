from django.urls import path
from . import views

urlpatterns = [
    path('', views.page, name='page' ),
    path('sign/', views.fomu, name='fomu' ),
    path('login/', views.ingia, name='ingia'),
    path('adsign/', views.adminfomu, name='adminfomu' ),
    path('ad/', views.ad, name='ad' ),
]