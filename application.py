from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def login():
    name = request.form.get("nombre")
    fecha = request.form.get("fecha")
    ciudad = request.form.get("ciudad")
    contraseña = request.form.get("contraseña")
    return render_template("session.html", name=name, fecha=fecha, ciudad=ciudad, contraseña=contraseña)

@app.route("/<string:name>")
def session(name):
    return render_template("session.html", name=name)

@app.route("/users")
def names():
    names = ["Jose","Pedro","Maria"]
    return render_template("list.html", names=names)

