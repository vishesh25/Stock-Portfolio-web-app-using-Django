from django.db import models
from django.contrib.auth.models import User
from . import stocks
from .utils import get_plot
import pandas as pd
# Create your models here.
FRUIT_CHOICES = [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]


class Stocks(models.Model):
    stock_name = models.CharField(max_length=50)
    purchased_price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=5)
    date_purchased = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolio')

    def current_price(self):
        current_price = float(str(stocks.stock_search(self.stock_name)).replace(',', ''))
        return current_price

    @property
    def quantityPercentage(self):
        total = self.user.portfolio.aggregate(total_quantity=models.Sum('quantity'))
        return "{0:.2f}".format((int(self.quantity) / total['total_quantity']) * 100)

    @property
    def get_current_price(self):
        current_price = stocks.stock_search(self.stock_name)
        return current_price

    @property
    def pie_chart(self):
        qs = self.user.portfolio.all()
        df = pd.DataFrame(qs.values())
        chart = get_plot(df, 'pie')
        return chart

    @property
    def bar_chart(self):
        qs = self.user.portfolio.all()
        df = pd.DataFrame(qs.values())
        df['current_price'] = [stocks.stock_search(name) for name in df['stock_name']]
        df['current_price'] = df['current_price'].str.replace(',', '').astype(float)
        df = df.sort_values(by=['current_price'], ascending=True)
        chart = get_plot(df, 'bar')
        return chart

    @property
    def profit_loss(self):
        result = self.current_price() - float(self.purchased_price)
        return "{0:0,.2f}".format(result)

    @property
    def total_profit_loss(self):
        result = (self.current_price() - float(self.purchased_price)) * int(self.quantity)
        return "{0:0,.2f}".format(result)



