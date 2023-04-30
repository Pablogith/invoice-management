from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    # User
    path('users-list/', views.UsersListView.as_view(), name='users_list'),
    path('user-add/', views.UserAdd.as_view(), name='user_add'),
    path('user-detail/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('user-delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
    path('user-update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    # Invoice
    path('invoice-pdf/<int:invoice_id>', views.generate_invoice, name='invoice_pdf'),
    path('invoice-list/', views.InvoicesListView.as_view(), name='invoices_list'),
    path('invoice-detail/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice_detail'),
    path('invoice-add/', views.InvoiceAdd.as_view(), name='invoice_add'),
    path('invoice-update/<int:pk>/', views.InvoiceUpdate.as_view(), name='invoice_update'),
    path('invoice-delete/<int:pk>/', views.InvoiceDelete.as_view(), name='invoice_delete'),
    # Product
    path('product-list/', views.ProductsListView.as_view(), name='products_list'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product-add/', views.ProductAdd.as_view(), name='product_add'),
    path('product-update/<int:pk>/', views.ProductUpdate.as_view(), name='product_update'),
    path('product-delete/<int:pk>/', views.ProductDelete.as_view(), name='product_delete'),
]
