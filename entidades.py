import csv
from google.cloud import language_v2
from google.cloud.language_v2 import Entity, EntityMention
from google.cloud.language_v2 import types
from claves import API_KEY_CNL

# Cliente de Google Cloud Natural Language
client = language_v2.LanguageServiceClient(
        client_options={"api_key": str(API_KEY_CNL)}
    )

# Listas para almacenar entidades detalladas
mis_entidades = []
entidades_resultados = []
entidades_faltantes = []

# Función para extraer entidades con opción de destino
def extract_entities(textos, lista_destino):
    lista = mis_entidades if lista_destino == "propia" else entidades_resultados

    entidades_existentes = {entidad["nombre"] for entidad in lista}  # Conjunto con nombres de entidades existentes

    for texto in textos:
        try:
            document = language_v2.Document(content=texto, type_=language_v2.Document.Type.PLAIN_TEXT)
            response = client.analyze_entities(request={"document": document})

            for entidad in response.entities:
                nombre_entidad = entidad.name
                
                if nombre_entidad not in entidades_existentes:  # Solo agregar si no existe
                    lista.append({
                        "nombre": nombre_entidad,
                        "tipo": language_v2.Entity.Type(entidad.type_).name,
                        "wiki_url": entidad.metadata.get("wikipedia_url", "Sin datos"),
                        "url_kgmid": f"https://www.google.com/search?q={nombre_entidad}&kponly&kgmid={entidad.metadata.get('mid', 'No existe id')}",
                    })
                    entidades_existentes.add(nombre_entidad)  # Agregar al conjunto para futuras verificaciones
        
        except Exception as e:
            print(f"Error al extraer entidades: {e}")

# Función para encontrar entidades faltantes
def encontrar_entidades_faltantes():
    """Encuentra entidades en los resultados que no están en la URL propia."""
    global entidades_faltantes
    nombres_mis_entidades = {ent["nombre"] for ent in mis_entidades}

    for entidad in entidades_resultados:
        if entidad["nombre"] not in nombres_mis_entidades:
            entidades_faltantes.append(entidad)

# Función para guardar entidades faltantes en CSV
def save_missing_entities_to_csv():
    """Guarda en un archivo CSV las entidades faltantes con todos sus datos."""
    if entidades_faltantes:
        with open("entidades_faltantes.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["nombre", "tipo", "wiki_url", "url_kgmid", "prominencia"])
            writer.writeheader()
            writer.writerows(entidades_faltantes)
        
        print(f"Archivo 'entidades_faltantes.csv' generado con {len(entidades_faltantes)} entidades faltantes.")
    else:
        print("No hay entidades faltantes.")
