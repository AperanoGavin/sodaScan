from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')


@app.route('/abdoutest')
def abdou():
    return render_template('test.html')


@app.route('/scan', methods=['POST'])
def scan():
    barcode = request.form['barcode']
    product_info = get_product_info(barcode)
    return jsonify(product_info)

def get_product_info(barcode):
    url = f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=90 , ssl_context=('/certs/fullchain.pem', '/certs/privkey.pem'))