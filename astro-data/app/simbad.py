from astroquery.simbad import Simbad
import pandas as pd

objetos = [
    "Vega"  # Vega
]

custom_simbad = Simbad()
custom_simbad.TIMEOUT = 60
custom_simbad.ROW_LIMIT = 0
custom_simbad.reset_votable_fields()
custom_simbad.add_votable_fields('otype', 'mesdistance', 'ra', 'dec', 'V', 'B', 'pmra', 'pmdec')

registros = []
falhas = []

for obj in objetos:
    try:
        result = custom_simbad.query_object(obj)
        if result is None or len(result) == 0:
            falhas.append(obj)
            continue
        
        row = result[0]
        registros.append({
            "Nome": obj,
            "Tipo": row["OTYPE"],
            "RA": str(row["RA"]),
            "DEC": str(row["DEC"]),
            "Distância_pc": row.get("MESDISTANCE"),
            "Mag_V": row.get("V"),
            "Mag_B": row.get("B"),
            "PM_RA": row.get("PMRA"),
            "PM_DEC": row.get("PMDEC"),
        })
    except Exception as e:
        print(f"Erro consultando '{obj}': {e}")
        falhas.append(obj)

if registros:
    df = pd.DataFrame(registros)
    print("\n🔭 Objetos encontrados no SIMBAD:\n")
    print(df.to_string(index=False))
else:
    print("⚠ Nenhum objeto retornou dados no SIMBAD.")

if falhas:
    print("\n❌ Objetos que não foram encontrados no SIMBAD:")
    print(", ".join(falhas))
