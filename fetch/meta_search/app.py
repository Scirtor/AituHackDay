
from flask import Flask, request, render_template, jsonify
from duckduckgo_search import DDGS

app = Flask(__name__)

@app.route("/images", methods=["GET", "POST"])
def images():
    ResultsImages = []
    query = ""
    if request.method == "POST":
        query = request.form.get("query")
        with DDGS() as ddgs:
            ResultsImages = ddgs.images(query, max_results=10)
    return ResultsImages
@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    query = ""
    if request.method == "POST":
        query = request.form.get("query")
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=10)
    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    app.run(debug=True)
