from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import requests
import json
# Create your views here.


def home_view(request):
    context = {}
    template_name = 'home.html'
    return render(request, template_name, context)

# Create your models here.


def convertCurrency(amount, fromCurrency, toCurrency):
    apiKey = '4ed858fd053071297e9d'
    fromCurrency = fromCurrency
    toCurrency = toCurrency
    query = fromCurrency + "_" + toCurrency
    url = 'https://free.currencyconverterapi.com/api/v6/convert?q=' + query + '&compact=ultra&apiKey=' +apiKey
    print(url)
    response = requests.get(url) 
    json_response = response.json()
    return json_response[query]

# print(convertCurrency(10, 'USD', 'PHP'))
    

# class ExpenseAddView(LoginRequiredMixin, CreateView):
#     model = Expense
#     form_class = ExpenseForm
#     # fields =['value',"reason","date_expense_was_made"]
#     success_url = reverse_lazy("expense:expenses_list")
#     template_name = 'expenses/new.html'
#     login_url = reverse_lazy('account:login')
    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.value = 
#         return super(ExpenseAddView, self).form_valid(form)

@login_required(login_url = reverse_lazy('account:login'))
def expense_add_view(request):
    import re
    template_name = 'expenses/new.html'
    context = {}
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            reason = form.cleaned_data['reason']
            date_expense_was_made = form.cleaned_data['date_expense_was_made']
            new_val =re.sub(' +', ' ',value)
            new_val_2 = [i for i in new_val.strip(" ").split(" ")]
            conversion = convertCurrency(float(new_val_2[0]), new_val_2[1].upper(), "GBP")
            Expense.objects.create(
                user = request.user,
                value = conversion,
                reason = reason,
                date_expense_was_made = date_expense_was_made
            )
            # print(conversion)
            return HttpResponseRedirect("/expenses/list")
    else:
        form = ExpenseForm()
    context['form'] = form
    return render(request, template_name, context)

class ExpenseListView(LoginRequiredMixin,ListView):
    model = Expense
    template_name ='expenses/list.html'
    login_url = reverse_lazy('account:login')
    

    def get_queryset(self):
        '''
        Generic Mixin
        Queries the the expenses by the user{User} 
        '''
        qs = super(ExpenseListView, self).get_queryset()
        # user = TeacherProfile.objects.get(user=self.request.user)
        return qs.filter(user=self.request.user)
