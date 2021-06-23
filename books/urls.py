from django import urls
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views 

urlpatterns = [
    path('', views.homepage, name="home"),
    path('accounts/', include('registration.backends.default.urls')),
    path('profile/', views.profile_page, name='profile_page'),
    path('collection/', views.book_list, name='book_list'),
    path('collection/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('collection/<int:pk>/delete', views.book_delete, name='book_delete'),
    path('collection/categories/<slug:slug>', views.show_category, name='show_category'),
]