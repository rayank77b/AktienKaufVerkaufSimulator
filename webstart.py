from flask import Flask
from flask import render_template
import sqlite3
import yfinance as yf

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
    conn = sqlite3.connect(db_name)
    sql = "SELECT ISIN, Name from Tickers WHERE ISIN ='%s'"%isin
    cursor = conn.execute(sql)
    data['isin'] = isin
    for row in cursor:
        data['name'] = row[1]
    conn.close()
    stock = yf.Ticker(isin)
    price = stock.info['currentPrice']
    data['price'] = price
    return render_template('isin.html', data = data)
    
if __name__ =='__main__':
    app.run(debug = WE_DEBUG)    
