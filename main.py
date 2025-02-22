# Comparador de entidades by: Jorge Hudson
# Librerías
import requests
from claves import API_KEY, CX
from scraper import scrape_url, scrape_results

def search_google(query, num_results=5):
    """Realiza una búsqueda en Google usando Custom Search Engine API."""
    url = "https://www.googleapis.com/customsearch/v1"
    
    params = {
        "key": API_KEY,
        "cx": CX,
        "q": query,
        "num": num_results  # Número de resultados
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        results = response.json().get("items", [])
        return results
    else:
        print("Error en la solicitud:", response.status_code)
        return []

if __name__ == "__main__":
    # Pide la URL de la web del usuario
    url = input("Ingresa la URL de tu página web: ")

    # Pide la consulta para buscar en Google
    consulta = input("Ingresa tu búsqueda en Google: ")
    resultados = search_google(consulta)

    if resultados:
        urls_resultados = [resultado['link'] for resultado in resultados]  # Lista de URLs

        # Muestra los resultados encontrados
        for i, resultado in enumerate(resultados, start=1):
            print(f"{i}. {resultado['title']}\n   {resultado['link']}\n")

        # Scrapeo y análisis de entidades de los resultados de búsqueda
        scrape_results(urls_resultados)

        # Scrapeo y análisis de entidades de la URL propia
        scrape_url(url)

    else:
        print("No se encontraron resultados.")
