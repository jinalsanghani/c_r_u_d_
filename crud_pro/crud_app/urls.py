from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.user_create, name='user_create'),
    path('list/', views.user_list, name='user_list'),
    path('user/<int:user_id>/update/', views.update_user, name='update_user'),
    path('user/<int:user_id>/delete/', views.delete_user, name='delete_user'),
]