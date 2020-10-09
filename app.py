from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index(): #home page index.html
    return render_template('index.html')

@app.route("/about")
def about(): #home page index.html
    return render_template('about.html',title="About")

@app.route("/fh4")
def fh4(): #home page index.html
    return render_template('fh4.html')

@app.route("/test")
def test(): #home page index.html
    return render_template('index2.html')
if __name__=='__main__':
    app.run(debug=True)


