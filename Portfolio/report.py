import pandas as pd
import sqlite3
from . import stocks


def generate_csv(request):
    try:
        con = sqlite3.connect("db.sqlite3")
        df = pd.read_sql_query("Select stock_name AS 'Stock Name', purchased_price AS 'Purchased Amount in ₹', "
                               "quantity AS 'Quantity', date_purchased AS 'Date of Purchase' from Portfolio_stocks"
                               " WHERE user_id == " + str(request.user.id),
                               con)

        df['Purchased Amount in ₹'] = df['Purchased Amount in ₹'].astype('float')
        df['Current Price in ₹'] = [float(stocks.stock_search(name).replace(',', '')) for name in df['Stock Name']]
        df['Unrealised Profit/Loss in ₹'] = df['Current Price in ₹'] - df['Purchased Amount in ₹']
        df['Total Net Gain/Loss in ₹'] = (df['Current Price in ₹'] - df['Purchased Amount in ₹']) * df['Quantity'].astype('int')

        df.to_excel("Stock Report.xlsx")
        return True
    except Exception:
        raise Exception("Error")
