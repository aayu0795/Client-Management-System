from django.urls import path
from django.views.generic import TemplateView
from .views import Homepage, Dashboard, add_a_customer, BatchdataView

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('add_a_customer/', add_a_customer, name='add_a_customer'),
    path('batch_customer_data/', BatchdataView.as_view(),
         name='batch_customer_data')
]
