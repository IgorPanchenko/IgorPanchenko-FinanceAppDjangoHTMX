from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from tracker.filters import TransactionFilter
from tracker.models import Transaction

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')

@login_required
def transaction_list(request):
    transaction_filter = TransactionFilter(
        request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related('category')
    )
    total_income = transaction_filter.qs.get_total_income()
    total_expenses = transaction_filter.qs.get_total_expenses()
    context = {'filter': transaction_filter,
               'total_expenses': total_expenses,
               'total_income': total_income,
               'net_income': total_income - total_expenses}
    if request.htmx:
        return render(request, 'tracker/partials/transaction-container.html', context)
    return render(request, 'tracker/transaction-list.html', context)