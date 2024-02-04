from flask import Flask, request, json
from flask_cors import CORS
from kdv import gen_kdv, gen_spa_kdv, gen_spa_stkdv

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
CORS(app)

@app.route("/")
def index():
    ans = gen_kdv()
    return ans


@app.route("/generate/kdv", methods=['POST'])
def generate_kdv():
    data = json.loads(request.data)
    res = gen_spa_kdv(data["params"], data["data"])
    return res

@app.route("/generate/stkdv", methods=['POST'])
def generate_stkdv():
    data = json.loads(request.data)
    res = gen_spa_stkdv(data["params"], data["data"])
    return res



if __name__ == '__main__':
    app.run(debug=True)