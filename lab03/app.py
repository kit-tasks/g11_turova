from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/<string:page_name>')
def page(page_name='form.html'):
    return render_template(page_name)

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
@app.route('/calc', methods=['GET'])
def simple_calc():
    var_1 = request.args.get("paramA", type=int)
    var_2 = request.args.get("paramB", type=int)
    opperation = request.args.get("op")
    

    if (opperation == "add"):
        res = var_1 + var_2
        doc =''
        doc += '<html lang = "ru">'
        doc += '<head>'
        doc += '</head>'
        doc += '<body>'
        doc += '<h1> result with GET method </h1>'
        doc += '<hr>'
        doc += f'hello, {res} {var_1} {var_2}!'
        doc += '</body>'
        doc += '</html>'
        return doc
        
        #print(var_1 + '+' +  var_2 + "="  + res)




if __name__ == '__main__':
    app.run(port=8080)
