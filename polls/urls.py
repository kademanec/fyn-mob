from django.urls import path

from . import views

urlpatterns = [
    path('', views.pricingConfig_list, name='pricingconfig-list'),
    path('create/', views.create_pricingModule, name='create-pricingModule'),
    path('edit/', views.edit_pricingModule, name='edit-pricingModule'),
    path('delete/', views.delete_pricingModule, name='delete-pricingModule'),
]