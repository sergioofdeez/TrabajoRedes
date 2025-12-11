import requests

API_KEY = "50bc79ccbc5149dca4da625c8e962399"

# -----------------------------------------------
# 1) Buscar recetas a partir de ingredientes
# -----------------------------------------------

def buscar_recetas(ingredientes, numero=5):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": ingredientes,
        "number": numero,
        "apiKey": API_KEY
    }

    respuesta = requests.get(url, params=params)
    datos = respuesta.json()

    return datos


# -----------------------------------------------
# 2) Obtener información completa de una receta
# -----------------------------------------------

def obtener_info_receta(id_receta):
    url = f"https://api.spoonacular.com/recipes/{id_receta}/information"
    params = {
        "includeNutrition": True,
        "apiKey": API_KEY
    }

    respuesta = requests.get(url, params=params)
    datos = respuesta.json()

    return datos


# -----------------------------------------------
# 3) Mostrar resultados de forma ordenada
# -----------------------------------------------

def mostrar_recetas(recetas):
    print("\n--- Recetas encontradas ---")
    for i, r in enumerate(recetas):
        print(f"{i+1}. {r['title']}")
    print()


def mostrar_ingredientes(ingredientes):
    print("\n--- Ingredientes de la receta ---")
    for ing in ingredientes:
        nombre = ing["name"]
        cantidad = ing["amount"]
        unidad = ing["unit"]
        
        
        print(f"- {nombre}: {cantidad} {unidad}")


def mostrar_nutricion(nutricion):
    print("\n--- Información nutricional de la receta completa---")
    for n in nutricion["nutrients"]:
        print(f"{n['name']}: {n['amount']} {n['unit']}")


def mostrar_nutricion_ingredientes(ingredientes):
    #devuelve la informacion nutricional de cada ingrediente por separado
    print("\n--- Información nutricional de cada ingrediente ---")
    for ing in ingredientes:
        #print("Buscando informacion sobre", ing["name"],"...")
        nombre_ingrediente = ing["name"]
        obtener_info_ingrediente(nombre_ingrediente) #hace una consulta para obtener los nutrientes a partir de ese nombre
    print()
    

def obtener_info_ingrediente(nombre):
    url = "https://api.api-ninjas.com/v1/nutrition"

    headers = {
        "X-Api-Key": "F6c0L7+BtM1butfWScFz0g==2FTLe3vkuuu5lCWD"
    }

    params = {
        "query": nombre
    }

    r = requests.get(url, headers=headers, params=params)

    # Comprueba si la petición fue bien
    if r.status_code != 200:
        print("No se ha podido obtener")
        return None

    data = r.json()  # Esto es una lista de dicts

    if not data:
        print("No se ha encontrado el", nombre)
        return None  # No encontró el ingrediente

    nutrientes = data[0]  # Devuelve el primer resultado
    print(str(nutrientes['name']).upper(),":", sep="")
    print("\t- Grasas(por cada 100g): ",nutrientes['fat_total_g'],"g",sep="")
    print("\t- Grasas saturadas(por cada 100g): ",nutrientes['fat_saturated_g'],"g",sep="")
    print("\t- Hidratos de carbono(por cada 100g): ",nutrientes['carbohydrates_total_g'],"g",sep="")
    print("\t- Azucares(por cada 100g): ",nutrientes['sugar_g'],"g",sep="")
    

# -----------------------------------------------
# 4) Programa principal
# -----------------------------------------------

def main():
    print("=== Buscador de recetas por ingredientes ===\n")

    ingredientes = input("Introduce ingredientes separados por coma (ej: pollo, arroz, tomate): ")

    # Buscar recetas
    recetas = buscar_recetas(ingredientes)

    if not recetas:
        print("No se encontraron recetas con esos ingredientes.")
        return

    # Mostrar lista al usuario
    mostrar_recetas(recetas)

    # Elegir receta
    opcion = int(input("Elige el número de una receta: ")) - 1
    receta_elegida = recetas[opcion]

    print(f"\nHas elegido: {receta_elegida['title']}")

    # Obtener detalles
    info = obtener_info_receta(receta_elegida["id"])

    # Ingredientes
    mostrar_ingredientes(info["extendedIngredients"])

    # Nutrición
    mostrar_nutricion(info["nutrition"])
    
    #Nutricion por ingredientes
    mostrar_nutricion_ingredientes(info["extendedIngredients"])


# Ejecutar programa
main()
