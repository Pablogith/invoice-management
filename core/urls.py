from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    # ex: /
    path('', views.IndexView.as_view(), name='index'),
    # ex: /dashboard/
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    # ex: /users-list/
    path('users-list/', views.UsersListView.as_view(), name='users_list'),
    # ex: /user-add/
    path('user-add/', views.UserAdd.as_view(), name='user_add'),
    # ex: /user/5
    path('user-detail/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    # ex: /user-delete/2
    path('user-delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
    # ex: /user-update/2
    path('user-update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
]
