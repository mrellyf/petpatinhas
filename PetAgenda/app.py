from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html")

@app.route("/listar")
def listar():
    return render_template("listar.html")

if __name__ == "__main__":
    app.run(debug=True)