from astropy.utils.data import get_pkg_data_filename
from astropy.table import Table
from astropy.io import fits

event_filename = get_pkg_data_filename('TILEY_18_SAMIKROSS_TFR_V1.fits')

fits.info(event_filename)
"""
events = Table.read(event_filename, hdu=1)

print(events.columns)

print(events['ID'])
"""

fits.setval(event_filename, 'OBJECT', value='M31')
