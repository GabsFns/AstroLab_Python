from astropy.io import fits
import pandas as pd

# caminho do arquivo FITS baixado localmente
filename = 'path/to/neowise_catalog.fits'

with fits.open(filename) as hdul:
    data = hdul[1].data  # dados na extensão 1 do FITS
    df = pd.DataFrame(data.byteswap().newbyteorder())  # converte para DataFrame Pandas

print(df.head())