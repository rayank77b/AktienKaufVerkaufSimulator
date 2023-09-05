from flask import Flask
from flask import render_template
import yfinance as yf
import sqlite3

db_name = 'db/Stocks.DB.sql3'


WE_DEBUG = True

app = Flask(__name__) 

@app.route('/') 
def root_index():  
    return "here we start";  

@app.route('/stocks') 
def stocks_index():
    conn = sqlite3.connect(db_name)
    cursor = conn.execute("SELECT ISIN, Name from Tickers")
    stocks = {}
    for row in cursor:
        stocks[row[0]] = row[1]
    conn.close()
    return render_template('stocks.html', stocks = stocks)

@app.route('/isin/<isin>') 
def isin_name_info(isin):
    data = {}
    volumes = {}
    prices = {}
    
    conn = sqlite3.connect(db_name)
    cursor = conn.execute("SELECT ISIN, Name from Tickers WHERE ISIN = ?", (isin,))
    data['isin'] = isin
    for row in cursor:
        data['name'] = row[1]
    
    stock = yf.Ticker(isin)
    price = stock.info['currentPrice']
    data['price'] = price
    
    cursor = conn.execute("SELECT * from my_stock_values WHERE ISIN = ?", (isin,))
    sqldata = cursor.fetchall()
    if len(sqldata)==0:
        data['we_have_it'] = 0
    else:
        data['we_have_it'] = 1
        cnt = 0
        for row in sqldata:
            volumes[cnt] = row[2]
            prices[cnt] = row[1]
            cnt = cnt + 1
    
    conn.close()
    return render_template('isin.html', data = data, volumes = volumes, prices = prices)

if __name__ =='__main__':
    app.run(debug = WE_DEBUG)    
