import os
from astroquery.vizier import Vizier
import pandas as pd

def fetch_neowise():
    # Configura para não limitar o número de linhas
    Vizier.ROW_LIMIT = -1  

    # Código do catálogo NEOWISE no VizieR
    catalog_code = "II/328"

    # Pasta destino
    data_neowise = os.path.join("datasets", "neowise")
    os.makedirs(data_neowise, exist_ok=True)

    # Nome do arquivo local
    arquivo_csv = os.path.join(data_neowise, "neowise_catalog.csv")

    # Baixar catálogo
    print("📡 Baixando dados NEOWISE do VizieR...")
    result = Vizier.get_catalogs(catalog_code)
    df = result[0].to_pandas()

    # Salvar localmente para uso offline
    df.to_csv(arquivo_csv, index=False)
    print(f"✅ Catálogo salvo em {arquivo_csv}")

    return df

# Exemplo de uso
if __name__ == "__main__":
    df_neowise = fetch_neowise()
    print(df_neowise.head())
    print(f"Total de linhas: {len(df_neowise)}")