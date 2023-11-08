from flask import Flask, request

app = Flask(__name__)

@app.route('/HelloNameGet', methods = ['GET'])
def HelloNameGet():
    value = request.args.get('param')
    doc = ''
    doc += '<!doctype html>'
    doc += '<html lang = "ru">'
    doc += '<head>'
    doc += '</head>'
    doc += '<body>'
    doc += '<h1> result with GET method </h1>'
    doc += '<hr>'
    doc += 'hello, ' + value + '!'
    doc += '</body>'
    doc += '</html>'
    return doc



    
