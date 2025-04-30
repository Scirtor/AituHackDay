from flask import Flask, request, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from duckduckgo_search import DDGS

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per minute"]
)

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
    filter_type = request.form.get("filter")
    if request.method == "POST":
        query = validate_query(request.form.get("query"))
        with DDGS() as ddgs:
            if filter_type == "images":
                results = [{"image": r["image"], "title": r["title"], "href": r["source"]} for r in ddgs.images(query, max_results=20)]
            elif filter_type == "videos":
                # Здесь можно добавить обработку видео, если библиотека поддерживает
                results = [{"title": "Видео не поддерживается", "href": "#", "body": "Функция видео пока не реализована."}]
            else:
                results = [{"title": r["title"], "href": r["href"], "body": r["body"]} for r in ddgs.text(query, max_results=20)]
    return render_template("index.html", results=results, query=query, filter=filter_type)

def validate_query(query):
    forbidden_keywords = ["--", ";", "DROP", "DELETE"]
    for keyword in forbidden_keywords:
        if keyword in query.upper():
            raise ValueError("Запрос содержит запрещённые символы.")
    return query



if __name__ == "__main__":
    app.run(debug=True)
