from flask import Flask, request, send_file
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

html_path = 'static/'
db_path = 'db/'

@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to Evro!</h1>"

@app.route('/db', methods=['GET', 'POST'])
def files():
    file_name = request.args.get('name')
    fp = db_path + file_name + '.txt'
    if request.method == 'GET':
        return send_file(fp)
    if request.method == 'POST':
        data = request.get_data()
        with open(fp, 'w') as file:
            file.write(data)
        return data

@app.route('/static', methods=['GET'])
def load_index_html():
    return send_file(html_path + 'index.html')

app.run(host='0.0.0.0', port=5000)
