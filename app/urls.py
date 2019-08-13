from django.urls import path, re_path
from . import views

urlpatterns = [
    path('data', views.Data.as_view()),
    path('secure/data', views.SecureData.as_view()),
    path('delay/data', views.DelayData.as_view()),
    path('user', views.UserDetail.as_view()),
]