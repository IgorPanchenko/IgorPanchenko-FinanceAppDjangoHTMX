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
        queryset=Transaction.objects.filter(user=request.user)
    )
    context = {'filter': transaction_filter}
    return render(request, 'tracker/transaction-list.html', context)