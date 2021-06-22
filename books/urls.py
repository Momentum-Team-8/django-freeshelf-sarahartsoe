from django import urls
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views 

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('accounts/', include('registration.backends.default.urls')),
]