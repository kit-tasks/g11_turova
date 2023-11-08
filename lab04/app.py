from flask import Flask, request

app = Flask(__name__)

@app.route('/checkboxes', methods = ['GET'])
def checkboxes():
    if "opt1" not in request.args:
        return "option 1 is not selected"
    opt2 = request.args.get("opt2")
    if opt2 == None:
        return "option 2 is not selected"
    return "booth options selected"

@app.route('/radiobuttons')
def radiobuttons():
    grp1 = request.args.get('grp1')
    if grp1 == None:
        return 'nothing selected in group 1'
    return  grp1 + ' selected in group 1 '
