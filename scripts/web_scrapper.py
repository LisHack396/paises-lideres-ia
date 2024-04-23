import requests
from bs4 import BeautifulSoup


def obtener_datos_web():
    """Extrae los datos de la pagina web"""
    url = "https://www.viaempresa.cat/es/ranking/ranking-paises-ia_2189603_102.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) "
                        "Chrome/107.0.0.0 Safari/537.36"
    }
    request = requests.get(url, headers=headers)
    if request.status_code != 200:
        print("Error al obtener datos", request.status_code)
    soup = BeautifulSoup(request.text, "html.parser")
    lista = soup.find_all("td")[3::]
    return [row.text for row in lista]