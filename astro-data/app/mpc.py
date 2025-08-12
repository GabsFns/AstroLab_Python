import requests
import zipfile
import io
import os

def fetch_and_store():
    url = "https://minorplanetcenter.net/Extended_Files/mpcorb.zip"
    response = requests.get(url)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            # cria pasta se não existir
            os.makedirs("mpc_data", exist_ok=True)
            z.extractall("mpc_data")
        return {"msg": "Arquivo MPCORB baixado e extraído com sucesso"}
    else:
        return {"erro": f"Erro ao baixar arquivo: {response.status_code}"}
    
if __name__ == "__main__":
    print(fetch_and_store())
    
    
    
