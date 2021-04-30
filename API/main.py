from flask import Flask, request
from crypto import encode, decode
app = Flask(__name__)


@app.route('/encode')
def encode_page():
    string: str = request.args.get('string', 'None')
    return encode(string)


@app.route('/decode')
def decode_page():
    key: str = request.args.get('key', 'None')
    string: str = request.args.get('string', 'None')
    if key == "None":
        return {"error": True, "status": 400, "message": "no key was provided. CDO804719"}
    else:
        return decode(string, key)


@app.route('/')
def main_page():
    return "NO PAGE HERE"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
