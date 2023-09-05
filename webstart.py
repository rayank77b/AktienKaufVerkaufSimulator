from flask import Flask
from flask import render_template
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

    
if __name__ =='__main__':
    app.run(debug = WE_DEBUG)    
