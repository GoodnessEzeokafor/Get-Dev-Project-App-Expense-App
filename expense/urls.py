from django.urls import path
from . import views


app_name = "expense"
urlpatterns = [
    path('new', views.expense_add_view, name="expense_new"),
    path('list', views.ExpenseListView.as_view(), name='expenses_list'),
]
