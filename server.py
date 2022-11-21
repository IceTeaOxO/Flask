from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

#simple backend
@app.route("/backend")
def backend():
    appInfo = {
        'id':1,
        'version':"1.1",
        'name':"Python",
    }
    return render_template('backend.html',appInfo=appInfo,text="this is text")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)