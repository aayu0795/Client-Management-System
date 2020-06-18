from django.urls import path
from django.views.generic import TemplateView
from .views import Homepage

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html')),
]
