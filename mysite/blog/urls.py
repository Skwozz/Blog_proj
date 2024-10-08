from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='create'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # path('login/', views.login_view, name='login'),
    # path('register/', views.register_view, name='register'),
    # path('logout/', views.logout_view, name='logout'),
]