from django import forms
from tracker.models import Transaction, Category


class TransactionForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.RadioSelect())

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise forms.ValidationError('Число должно быть положительным')
        return amount

    class Meta:
        model = Transaction
        fields = ('type', 'amount', 'date', 'category')
        widget = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
