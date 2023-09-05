from flask import Flask  

WE_DEBUG = True

app = Flask(__name__) 

@app.route('/') 
def root_index():  
    return "here we start";  

@app.route('/stocks') 
def stocks_index():
    return "here we start";  
    
if __name__ =='__main__':  
    app.run(debug = WE_DEBUG)    
