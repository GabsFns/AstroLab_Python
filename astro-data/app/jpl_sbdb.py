import requests
from time import sleep

def fetch_multiple_sbdb(object_ids):
    resultados = []
    
    for obj_id in object_ids:
        url = f"https://ssd-api.jpl.nasa.gov/sbdb.api?sstr={obj_id}&full-prec=true"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            resultados.append({
                "nome": data.get("object", {}).get("fullname"),
                "a": data.get("orbit", {}).get("elements", {}).get("a"),
                "e": data.get("orbit", {}).get("elements", {}).get("e"),
                "moid": data.get("orbit", {}).get("elements", {}).get("moid"),
                "H": data.get("phys_par", {}).get("H"),
                "albedo": data.get("phys_par", {}).get("albedo"),
                "diameter": data.get("phys_par", {}).get("diameter")
            })
        else:
            resultados.append({"erro": f"Erro {response.status_code} para {obj_id}"})
        
        sleep(0.5)  # boa prática para evitar bloqueio

    return resultados