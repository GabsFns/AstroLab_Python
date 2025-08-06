from astroquery.simbad import Simbad

def fetch_and_store():
    objetos = [
        "Vega", "Sirius", "Betelgeuse", "Antares", "Polaris", "Aldebaran", "Rigel", "Capella",
        "Deneb", "Altair", "Procyon", "Spica", "Arcturus", "Castor", "Pollux", "Fomalhaut",
        "Regulus", "Bellatrix", "Alnitak", "Alnilam", "Mintaka", "M33", "M42", "M45", "M31",
        "M81", "M82", "M87", "NGC 2244", "NGC 253", "NGC 891", "NGC 4565", "NGC 4631", "NGC 5055",
        "NGC 5194", "NGC 6946", "NGC 7331", "NGC 7479", "NGC 7793", "Denebola", "Alphard",
        "Zubenelgenubi", "Zubeneschamali", "Shaula", "Lesath", "Kaus Australis", "Kaus Media",
        "Kaus Borealis", "Alnasl"
    ]

    custom_simbad = Simbad()
    custom_simbad.TIMEOUT = 120
    custom_simbad.ROW_LIMIT = 0  # Sem limite de resultados
    custom_simbad.remove_votable_fields()
    custom_simbad.add_votable_fields(
        'otype', 'distance_result', 'ra', 'dec',
        'flux(V)', 'flux(B)', 'pmra', 'pmdec'
    )
    
    result = custom_simbad.query_objects(objetos)

    if result is None:
        return {"msg": "Nenhum dado SIMBAD retornado"}

    registros = []
    for row in result:
        registros.append({
            "nome": row["MAIN_ID"].decode() if isinstance(row["MAIN_ID"], bytes) else row["MAIN_ID"],
            "tipo": row["OTYPE"],
            "ra": str(row["RA"]),
            "dec": str(row["DEC"]),
            "distancia_pc": row.get("Distance_distance_result", None),
            "mag_v": row.get("FLUX_V", None),
            "mag_b": row.get("FLUX_B", None),
            "pm_ra": row.get("PMRA", None),
            "pm_dec": row.get("PMDEC", None),
        })

    return registros