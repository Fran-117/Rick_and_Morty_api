from flask import Flask, render_template   
import requests

app = Flask(__name__)

@app.route("/")

def personajes():
    url = "https://rickandmortyapi.com/api/character"   
    response = requests.get(url)
    data = response.json()

    personajes = []
    for personaje in data["results"]:
        personajes.append({
            "nombre": personaje["name"],
            "imagen": personaje["image"],
            "estado": personaje["status"]
        })

    return render_template("vista.html", personajes=personajes)

if __name__ == "__main__":
    app.run(debug=True)


