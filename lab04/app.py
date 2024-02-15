from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/good.html')
def good():
    return render_template("good.html")

@app.route('/five.html')
def five():
    return render_template("five.html")

@app.route('/checkboxesGet', methods = ['GET'])
def checkboxesGet():
    opt2 = request.args.get("opt2")
    opt1 = request.args.get("opt1")

    if "opt1" not in request.args:
        return "option 1 is not selected"
    elif "opt1" in request.args:
        return "option 1 was selected" 
    
@app.route('/checkboxesPost', methods = ['POST'])
def checkboxesPost():
    opt2 = request.form['opt2']
    opt1 = request.form['opt1']

    if "opt1" not in request.form.get:
        return "option 1 is not selected"
    elif "opt1" in request.form.get:
        return "option 1 was selected" 


@app.route('/radiobuttons')
def radiobuttons():
    grp1 = request.args.get('grp1')
    if grp1 == None:
        return 'nothing selected in group 1'
    return  grp1 + ' selected in group 1 '
