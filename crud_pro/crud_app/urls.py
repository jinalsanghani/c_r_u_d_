from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.user_list, name='user_list'),
    path('user/create/', views.user_create, name='user_create'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    # path('success/', views.success_view, name='success'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]

