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
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    return render_template("story.html",place=place,noun=noun,verb=verb,adjective=adjective,plural_noun=plural_noun)