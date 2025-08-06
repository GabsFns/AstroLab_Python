from astroquery.gaia import Gaia

def fetch_and_store():
    query = """
        SELECT TOP 10000
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

    # Executa a query no banco da Gaia
    job = Gaia.launch_job_async(query)
    results = job.get_results()

    # Retorna os dados em formato de dicionário (pode salvar no banco ou retornar via API)
    # return results.to_pandas().to_dict(orient="records")
    return results.to_pandas()

if __name__ == "__main__":
    df = fetch_and_store()
    
    # Nome do seu arquivo CSV (pode ser vazio, será sobrescrito)
    caminho_arquivo = "../data/gaia_data.csv"
    
    # Salva o DataFrame no CSV, sem índice e com vírgula como separador
    df.to_csv(caminho_arquivo, index=False)
    
    print(f"Arquivo '{caminho_arquivo}' salvo com sucesso!")