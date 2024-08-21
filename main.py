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

parsed_data = []
for ticker, news_table in news_tables.items():
    for row in news_table.findAll('tr'):
        title = row.a.text
        date_data = row.td.text.strip().split(' ')
        if len(date_data) == 1:
            time = date_data[0].strip()
        else:
            date = date_data[0].strip()
            time = date_data[1].strip()
        parsed_data.append([ticker, date, time, title])

print(parsed_data)