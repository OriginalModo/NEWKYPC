from .views import *
from django.urls import path



urlpatterns = [
    path('', news_home, name='news_home'),
    path('create', create, name='create'),
    path('<slug:slug>', NewsDetail.as_view(), name='detail'),
    path('<slug:slug_update>/update', NewsUpdateView.as_view(), name='update'),
    path('<slug:slug_delete>/delete', NewsDeleteView.as_view(), name='delete'),
]