from django import forms
from .models import Stocks
from .utils import get_listed_company

INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 100)]
LISTED_COMPANIES = get_listed_company()


class DateInput(forms.DateInput):
    input_type = 'date'


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = ('stock_name', 'purchased_price', 'quantity', 'date_purchased')
        labels = {
            'stock_name': 'Stock name',
            'date_purchased': 'Date of Purchase',
            'purchased_price': 'Price',
            'quantity': 'Stock Quantity'
        }
        widgets = {
            'stock_name': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'purchased_price': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'date_purchased': DateInput(attrs={'class': 'form-control my-3'})
        }

    stock_name = forms.CharField(widget=forms.Select(choices=LISTED_COMPANIES,
                                                     attrs={'class': 'form-control my-3'}))
    quantity = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES,
                                                      attrs={'class': 'form-control my-3'}))


class UpdatePortfolioForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = ('stock_name', 'purchased_price', 'quantity')
        labels = {
            'stock_name': 'Stock name',
            'purchased_price': 'Purchased Price',
            'quantity': 'Stock Quantity'
        }
        widgets = {
            'purchased_price': forms.TextInput(attrs={'class': 'form-control my-3'}),
        }

    stock_name = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    quantity = forms.IntegerField(label="Quantity",
                                  widget=forms.Select(choices=INTEGER_CHOICES,
                                                      attrs={'class': 'form-control my-2'}))
