from flask import Flask, request

app = Flask('__name__')

@app.route('/HelloName', methods = ['GET'])
def my_form():
    value = request.args.get('param')
    
