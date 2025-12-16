from flask import Flask, render_template   
import requests

app = Flask(__name__)

@app.route("/")

def personajes_y_episodios():
    url_personaje = "https://rickandmortyapi.com/api/character"
    url_episodio = "https://rickandmortyapi.com/api/episode"      
    response = requests.get(url_personaje)
    data = response.json()

    personajes = []
    for personaje in data["results"]:
        personajes.append({
            "nombre": personaje["name"],
            "imagen": personaje["image"],
            "genero": personaje["gender"],
            "lugar": personaje["origin"]["name"],
        })

    resultado = requests.get(url_episodio)
    dato = resultado.json()

    episodio = []
    for episodio in dato["results"]:
        episodio.append({
            "titulo": episodio["name"],
            "fecha": episodio["air_date"],
        })

    return render_template("vista.html", personajes=personajes, episodio=episodio)

if __name__ == "__main__":
    app.run(debug=True)


