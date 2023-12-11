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

@app.route('/HelloNamePost', methods=['GET', 'POST'])
def HelloNamePost():
    if request.method == 'GET':
        param = request.args.get['param']
        doc =''
        doc += '<html lang = "ru">'
        doc += '<head>'
        doc += '</head>'
        doc += '<body>'
        doc += '<h1> result with GET method </h1>'
        doc += '<hr>'
        doc += 'hello, ' + param + '!'
        doc += '</body>'
        doc += '</html>'
       
        return doc
    elif request.method == 'POST':
        param = request.form['param']
        doc =''
        doc += '<html lang = "ru">'
        doc += '<head>'
        doc += '</head>'
        doc += '<body>'
        doc += '<h1> result with POST method </h1>'
        doc += '<hr>'
        doc += 'hello, ' + param + '!'
        doc += '</body>'
        doc += '</html>'
        return doc
    else:
        return 'unknown method'

    
if __name__ == '__main__':
    app.run(port=8080)