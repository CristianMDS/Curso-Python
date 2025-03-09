import requests
from bs4 import BeautifulSoup

url = "https://dockerlabs.es/"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')

    maquinas = soup.find_all('div', onclick=True)

    for maquina in maquinas:
        onclick_txt = maquina["onclick"]
        nombre_maquina = str(onclick_txt.split("'")[1])
        dificultad = onclick_txt.split("'")[3]
        autor = onclick_txt.split("'")[7]
        print(f"Nombre de la maquina: [{nombre_maquina}] - Dificultad: [{dificultad}] - Autor: [{autor}]")

else:
    print("Error")