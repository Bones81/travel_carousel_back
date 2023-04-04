from django.urls import path
from . import views

urlpatterns = [
    path('api/photos', views.PhotoList.as_view(), name='photo_list'),
    path('api/photos/<int:pk>', views.PhotoDetail.as_view(), name='photo_detail'), 
]
