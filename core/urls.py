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
    # ex: /user/5
    path('user-detail/<int:user_id>/', views.UserDetailView.as_view(), name='user_detail'),
]
