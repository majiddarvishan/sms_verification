from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def main_page():
    return 'Hello'

# @app.route('/')
# def hello():
#     name = request.args.get("name", "World")
#     return f'Hello, {escape(name)}!'