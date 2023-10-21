from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}), required=False  
    )

    class Meta:
        model = Expense
        fields = ['date', 'category', 'amount', 'description', 'location']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
