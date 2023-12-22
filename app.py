from flask import Flask, request, json
from kdv import gen_kdv, gen_spa_kdv

app = Flask(__name__)

@app.route("/")
def index():
    ans = gen_kdv()
    return ans


@app.route("/generate", methods=['POST'])
def generate():
    data = json.loads(request.data)
    res = gen_spa_kdv(data["params"], data["data"])
    return res


if __name__ == '__main__':
    app.run(debug=True)