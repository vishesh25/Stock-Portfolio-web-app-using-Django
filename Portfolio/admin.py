from django.contrib import admin
from . import models
# Register your models here.


class StockAdmin(admin.ModelAdmin):
    list_display = ('stock_name', 'purchased_price', 'quantity', 'date_purchased',)


admin.site.register(models.Stocks, StockAdmin)
