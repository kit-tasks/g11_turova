from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
item = []



@app.route('/<string:page_name>')
def page(page_name='clock.html'):
    t = datetime.now()
    s = t.strftime('%H:%M:%S')
    return render_template(page_name, cur_time = s)

#@app.route('/list', methods = ['GET', 'POST'])
#def some_list():
 #   if request.method == 'POST':
  ##     item.append(text)

   # return render_template('list.html', text_items = item)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')