from flask import Flask, request

app = Flask(__name__)

@app.route('/checkboxes', methods = ['GET'])
def checkboxes():
    opt2 = request.args.get("opt2")
    opt1 = request.args.get("opt1")

    if "opt1" and  "opt2" not in request.args:
        return  " nothing"
    elif "opt1" not in request.args:
        return "option 1 is not selected"
    elif "opt2" not in request.args:
        return "option 2 is not selected"
    elif "opt1" and "opt2" in request.args:
        return "option 1 and option 2 was selected"


@app.route('/radiobuttons')
def radiobuttons():
    grp1 = request.args.get('grp1')
    if grp1 == None:
        return 'nothing selected in group 1'
    return  grp1 + ' selected in group 1 '
