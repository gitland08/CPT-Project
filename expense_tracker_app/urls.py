from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
    path('edit/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('demo/', views.demo, name='demo'),
]
