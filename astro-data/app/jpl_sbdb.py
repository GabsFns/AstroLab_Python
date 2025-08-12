import requests
from time import sleep

def fetch_multiple_sbdb(object_ids):
    resultados = []

    for obj_id in object_ids:
        url = f"https://ssd-api.jpl.nasa.gov/sbdb.api?sstr={obj_id}&full-prec=true"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Converte lista de elementos orbitais em dict para fácil acesso
            elementos = {el["name"]: el["value"] for el in data.get("orbit", {}).get("elements", [])}
            fisicos = data.get("phys_par", {})

            resultados.append({
                "nome": data.get("object", {}).get("fullname"),
                "a": elementos.get("a"),
                "e": elementos.get("e"),
                "moid": elementos.get("moid"),
                "H": fisicos.get("H"),
                "albedo": fisicos.get("albedo"),
                "diameter": fisicos.get("diameter")
            })
        else:
            resultados.append({"erro": f"Erro {response.status_code} para {obj_id}"})

        sleep(0.5)  # Evitar bloqueio

    return resultados

# Exemplo de uso
if __name__ == "__main__":
    lista = ["Ceres", "Vesta", "433 Eros"]
    dados = fetch_multiple_sbdb(lista)
    for d in dados:
        print(d)