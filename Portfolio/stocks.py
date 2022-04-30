import re
import urllib.request
from django.http import Http404


def stock_search(stockName):
    try:

        url = "https://www.google.com/finance/quote/{0}:NSE".format(stockName.upper())

        response = urllib.request.urlopen(url).read().decode('utf-8')
        stockSpan = re.search('<div class="YMlKec fxKbKc">', response)
        start = stockSpan.end()

        newResponse = response[start:start + 50]
        stockSpan = re.search("</div>", newResponse)
        end = stockSpan.start() - 1

        return newResponse[1:end]

    except Exception:
        raise Http404("Stock could not been found!")
