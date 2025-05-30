from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    try: 
        response = requests.get("https://api.jikan.moe/v4/top/anime?limit=25")
        data = response.json()
        top_anime = data.get('data', [])
    except:
        top_anime = []

    return render_template("index.html", anime_list=top_anime)

@app.route("/search", methods=["GET", "POST"])
def search():
    anime_list = []
    query = ""
    if request.method == "POST":
        query = request.form.get("query")
        try:
            response = requests.get(f"https://api.jikan.moe/v4/anime?q={query}&limit=25")
            data = response.json()
            anime_list = data['data']
        except:
            anime_list = []
    return render_template("search.html", anime_list=anime_list, query=query)

@app.route("/anime/<int:anime_id>")
def anime_detail(anime_id):
    try:
        response = requests.get(f"https://api.jikan.moe/v4/anime/{anime_id}")
        data = response.json().get("data")
    except:
        data = {}

    return render_template("anime.html", anime=data)

if __name__ == "__main__":
    app.run(debug=True)