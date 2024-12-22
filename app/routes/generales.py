from ..app import app
from flask import render_template


@app.route("/retrieve_wididata/<string:id>")
def retrieve_wikidata(id:str):
    return render_template("templates/retrieve_wikidata.html",http_code=200,content_type="ubvu")


app.run()