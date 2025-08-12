import os
import pandas as pd
from astroquery.vizier import Vizier

def fetch_panstarrs():
    Vizier.ROW_LIMIT = 5000  # limite inicial
    pan_starrs = os.path.join("datasets", "panstarrs")
    os.makedirs(pan_starrs, exist_ok=True)

    print("Baixando Pan-STARRS DR1 (MeanObject)...")
    tabela = Vizier.get_catalogs("II/349/ps1")
    df = tabela[0].to_pandas()

    panstarrs_csv = os.path.join(pan_starrs, "panstarrs_dr1.csv")
    df.to_csv(panstarrs_csv, index=False)
    print(f"Pan-STARRS salvo em {panstarrs_csv} ({len(df)} linhas)")

    return df

if __name__ == "__main__":
    fetch_panstarrs()