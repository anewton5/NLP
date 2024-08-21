from urllib.request import urlopen, Request;
from bs4 import BeautifulSoup;

finviz_url = 'https://finviz.com/quote.ashx?t='
tickers = [ 'AAPL','AMZN', 'MSFT', 'NVDA', 'IBM', 'BRK.B', 'JPM']

news_tables = {}

for ticker in tickers:
    url= finviz_url + ticker

    req = Request(url=url, headers={'User-Agent': 'my-app'})
    response = urlopen(req)
    html = BeautifulSoup(response, 'html')
    news_table = html.find(id='news-table')
    news_tables[ticker] = news_table
    break