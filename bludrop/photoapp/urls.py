from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('signup/',views.signup,name = 'signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('photo/',views.PhotoListView.as_view(),name='photo'),
    path('photo/<int:pk>',views.PhotoDetailView.as_view(),name='detail'),
    path('photo/create/',views.PhotoCreateView.as_view(),name='create'),
]