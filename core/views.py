from django.views import generic
from django.urls import reverse_lazy
from .models import User


class IndexView(generic.TemplateView):
    template_name = 'core/index.html'


class DashboardView(generic.TemplateView):
    template_name = 'core/dashboard.html'


class UsersListView(generic.ListView):
    model = User
    template_name = 'core/user/users_list.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        return User.objects.all()


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'core/user/user_detail.html'
    context_object_name = 'user'


class UserAdd(generic.CreateView):
    model = User
    fields = [
        'email',
        'first_name',
        'last_name',
        'street_address',
        'city',
        'country',
        'postal_code',
        'contact_information',
        'account_status',
    ]
    template_name = 'core/user/user_add.html'
    success_url = reverse_lazy('core:users_list')


class UserUpdate(generic.UpdateView):
    model = User
    fields = [
        'email',
        'first_name',
        'last_name',
        'street_address',
        'city',
        'country',
        'postal_code',
        'contact_information',
        'account_status',
    ]
    template_name = 'core/user/user_update.html'
    success_url = reverse_lazy('core:users_list')


class UserDelete(generic.DeleteView):
    model = User
    success_url = reverse_lazy('core:users_list')

