from django.urls import path
from django.views.generic import TemplateView
from .views import (
    Homepage,
    Dashboard,
    add_a_customer,
    add_batch_of_customers,
    CustomerDetailView,
    update_customer_detail,
    delete_customer,
)

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('add_a_customer/', add_a_customer, name='add_a_customer'),
    path('add_batch_of_customers/', add_batch_of_customers,
         name='add_batch_of_customers'),
    path('customer_detail/<pk>', CustomerDetailView.as_view(),
         name='customer_detail'),
    path('update_customer_detail/<int:id>', update_customer_detail,
         name='update_customer_detail'),
    path('delete_customer/<int:id>', delete_customer, name='delete_customer'),
]
