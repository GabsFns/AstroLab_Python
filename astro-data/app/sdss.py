import os
import pandas as pd
from astroquery.vizier import Vizier

def fetch_sdss():
    Vizier.ROW_LIMIT = 5000  # limite inicial para teste
    sdss_dataset = os.path.join("datasets", "sdss")
    os.makedirs(sdss_dataset, exist_ok=True)

    print("Baixando SDSS DR16 Photomdetric...")
    tabela = Vizier.get_catalogs("V/154/sdss16")
    df = tabela[0].to_pandas()

    arquivo_csv = os.path.join(sdss_dataset, "sdss_dr16.csv")
    df.to_csv(arquivo_csv, index=False)
    print(f"SDSS salvo em {arquivo_csv} ({len(df)} linhas)")

    return df

if __name__ == "__main__":
    fetch_sdss()