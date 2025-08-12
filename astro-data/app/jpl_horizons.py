import requests
import zipfile
import io
import os
from astroquery.jplhorizons import Horizons
from time import sleep
import pandas as pd
from tqdm import tqdm 

def baixar_e_extrair_mpc(url, pasta_destino="mpc_data"):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        os.makedirs(pasta_destino, exist_ok=True)
        arquivo_path = os.path.join(pasta_destino, "MPCORB.DAT")
        with open(arquivo_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("MPCORB baixado e salvo com sucesso em", arquivo_path)
    else:
        raise Exception(f"Erro ao baixar arquivo: {response.status_code}")

def extrair_ids_arquivo_mpc(arquivo_path, max_ids=50):
    ids = []
    with open(arquivo_path, 'r', encoding='utf-8', errors='ignore') as f:
        for linha in f:
            id_objeto = linha[:7].strip()
            if id_objeto and id_objeto not in ids:
                ids.append(id_objeto)
            if len(ids) >= max_ids:
                break
    print(f"{len(ids)} IDs extraídos do arquivo MPC.")
    return ids

def baixar_ephemerides_jpl(ids, pasta_destino="horizons_data", start_date="2025-01-01", stop_date="2025-01-05"):
    os.makedirs(pasta_destino, exist_ok=True)
    for obj_id in tqdm(ids, desc="Consultando objetos JPL"):
        try:
            obj = Horizons(id=obj_id, location='500', epochs={'start': start_date, 'stop': stop_date, 'step': '1d'})
            eph = obj.ephemerides()
            df = eph.to_pandas()

            arquivo_csv = os.path.join(pasta_destino, f"{obj_id}.csv")
            df.to_csv(arquivo_csv, index=False)
        except Exception as e:
            print(f"\nErro ao consultar objeto {obj_id}: {e}")
        sleep(1)  # evita banimento por consultas rápidas

if __name__ == "__main__":
    url_mpc = "https://minorplanetcenter.net/iau/MPCORB/MPCORB.DAT"

  
    baixar_e_extrair_mpc(url_mpc)

 
    arquivo_mpcorb = "mpc_data/MPCORB.DAT"
    ids_objetos = extrair_ids_arquivo_mpc(arquivo_mpcorb, max_ids=20)  

  
    baixar_ephemerides_jpl(ids_objetos)