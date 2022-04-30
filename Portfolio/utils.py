import matplotlib.pyplot as plt
import base64
from io import BytesIO
import pandas as pd
import sqlite3
from .stocks import stock_search


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(df, chart_type):
    plt.switch_backend('AGG')
    if chart_type.lower() == 'pie':
        plt.title('Stock vs Quantity')
        plt.pie(df['quantity'], labels=df['stock_name'],
                autopct=lambda p: f'{p:.2f}%, {p * sum(df["quantity"].astype("int")) / 100 :.0f} items')
    elif chart_type.lower() == 'bar':
        x = df['stock_name']
        y = df['current_price']
        plt.barh(x, y)
        plt.title('Stock vs price bar chart')
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_plot_bar(x, y):
    plt.switch_backend('AGG')
    data = {'Price': ['Current Price', 'Purchased Price'],
            'Values': [y, x]}
    df = pd.DataFrame(data)
    plt.bar(df['Price'], df['Values'], color=['yellow', 'red'])
    plt.title('Purchased Amount vs Current Value')
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_listed_company():
    con = sqlite3.connect("db.sqlite3")
    df = pd.read_sql_query("Select Symbol AS 'Symbol', Name_of_company AS 'Name of Company' from Listed_companies", con)
    listed_company = []
    for x, y in df.itertuples(index=False):
        tup = (x, y)
        listed_company.append(tup)
    return listed_company


def get_total_purchased_price(request):
    total_price = 0
    purchase = request.user.portfolio.all().values('purchased_price', 'quantity')
    for name in purchase:
        price = 1
        for value in name.values():
            price *= int(value)
        total_price += price
    return total_price


def get_total_current_price(request):
    total_price = 0
    purchase = request.user.portfolio.all().values('stock_name', 'quantity')
    for name in purchase:
        price = 0
        for key, value in name.items():
            if key == "stock_name":
                price += float(str(stock_search(value)).replace(",", ""))
            else:
                price *= int(value)
        total_price += price
    return total_price
