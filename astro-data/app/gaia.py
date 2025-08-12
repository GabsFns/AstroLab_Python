from astroquery.gaia import Gaia
import pandas as pd
from tqdm import tqdm
import time

def fetch_and_store():
    query = """
        SELECT TOP 80000
            source_id,
            ra, dec,
            parallax, parallax_error,
            pmra, pmra_error,
            pmdec, pmdec_error,
            radial_velocity,
            phot_g_mean_mag,
            phot_bp_mean_mag,
            phot_rp_mean_mag,
            phot_g_mean_flux_error,
            astrometric_excess_noise,
            astrometric_gof_al,
            visibility_periods_used
        FROM gaiadr3.gaia_source
        WHERE phot_g_mean_mag < 15
        AND parallax IS NOT NULL
        AND visibility_periods_used > 8
    """

   
    job = Gaia.launch_job_async(query)

    # Barra de progresso personalizada
    with tqdm(total=100, desc="🔭 Consultando Gaia", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}%", colour="cyan") as pbar:
        while job.get_phase() not in ["COMPLETED", "ERROR"]:
        
            if pbar.n < 90:
                pbar.update(1)
            time.sleep(0.3)

       
        pbar.n = 100
        pbar.refresh()

    
    results = job.get_results()
    return results.to_pandas()

if __name__ == "__main__":
    df = fetch_and_store()
    
    caminho_arquivo = "../data/gaia_data.csv"
    df.to_csv(caminho_arquivo, index=False)
    
    print(f"\n Arquivo '{caminho_arquivo}' salvo com sucesso!")
