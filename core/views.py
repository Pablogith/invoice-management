from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'core/index.html'


class DashboardView(generic.TemplateView):
    template_name = 'core/dashboard.html'


class UsersListView(generic.TemplateView):
    template_name = 'core/users_list.html'


class UserDetailView(generic.TemplateView):
    template_name = 'core/user_detail.html'
