from flask import Flask, request
from query import get_company_information
from query_walapop import get_walapop
app = Flask(__name__)

@app.route('/')
def hello_world():
    return ' Hello World!'\

@app.route('/api/yahoo')
def get_company():
    symbol = "DIS"
    return get_company_information(symbol)

@app.route('/api/walapop')
def get_product_and_price_average():
    query = request.args.get('search_text')
    return get_walapop(query)

if __name__ == '__main__':
    app.run()
