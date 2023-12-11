from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<string:page_name>')
def page (page_name = "index.html"):
    return render_template(page_name)

if __name__ == '__main__':
    app.run(port=8080)
    