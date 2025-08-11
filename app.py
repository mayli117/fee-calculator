from flask import Flask, request, jsonify
from parser import parse_contract_file
from utils import calculate_fees
app = Flask(__name__)
@app.route('/upload', methods=['POST'])
def upload():
   file = request.files['file']
   data = parse_contract_file(file)
   return jsonify(data)
@app.route('/calculate', methods=['POST'])
def calculate():
   payload = request.json
   result = calculate_fees(payload)
   return jsonify(result)
if __name__ == '__main__':
   app.run(debug=True)
