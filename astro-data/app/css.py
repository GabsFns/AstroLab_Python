import os
import requests

def fetch_css_dr2():
    url = "https://nesssi.cacr.caltech.edu/DataRelease/VarStar/CSS_DR2_variables.csv"
    pasta_destino = os.path.join("datasets", "css")
    os.makedirs(pasta_destino, exist_ok=True)
    arquivo_csv = os.path.join(pasta_destino, "css_dr2_variables.csv")

    if not os.path.exists(arquivo_csv):
        print(f"📡 Baixando CSS DR2 Variáveis de {url} ...")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(arquivo_csv, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"✅ CSS DR2 Variáveis salvo em {arquivo_csv}")
        else:
            raise Exception(f"Erro ao baixar CSS DR2: {response.status_code}")
    else:
        print(f"Arquivo já existe: {arquivo_csv}")

    return arquivo_csv

if __name__ == "__main__":
    path = fetch_css_dr2()
    print(f"Arquivo pronto para uso: {path}")