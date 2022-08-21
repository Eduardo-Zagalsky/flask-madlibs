from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-phrase"
debug = DebugToolbarExtension(app)

@app.route("/")
def mad_libs():
    return render_template("madlibs.html")

@app.route("/story")
def story():
    return render_template("story.html")