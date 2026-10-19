import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    daftar_lagu = []
    keyword = ""

    if request.method == "POST":
        keyword = request.form.get("pencarian")
        url = f"https://itunes.apple.com/search?term={keyword}&entity=song&limit=5"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            daftar_lagu = data.get("results", [])

    return render_template("index.html", lagu=daftar_lagu, keyword=keyword)

if __name__ == "__main__":
    app.run(debug=True)