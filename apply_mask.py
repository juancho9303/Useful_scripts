from astropy.utils.data import get_pkg_data_filename
import astropy
from astropy.table import Table
from astropy.io import fits
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
from astropy.io.fits import getheader

#fullfile = get_pkg_data_filename('007_ready_intento_1_comp.fits')
velmap = get_pkg_data_filename('velocity_map.fits')
halpha = get_pkg_data_filename('halpha.fits')
halphaerror = get_pkg_data_filename('halpha_error.fits')

hdu1 = fits.open(velmap)
hdu2 = fits.open(halpha)
hdu3 = fits.open(halphaerror)
data1 = hdu1[0].data
data2 = hdu2[0].data
data3 = hdu3[0].data
datamask = data2/data3
data1[datamask<0.09]=np.nan
data1[data2>1]=np.nan
data2[data2>2.5]=np.nan
data1[data1>200]=np.nan
data1[data1<-200]=np.nan
#data2[np.isnan(data2)] = -5

fig, (ax1, ax2) = plt.subplots(figsize=(9, 4), ncols=2)
velmapplot = ax1.imshow(data1, cmap=mpl.cm.seismic, interpolation='none')
ax1.set_title('Velocity Map')
fig.colorbar(velmapplot, ax=ax1)

halphaplot = ax2.imshow(data2, cmap=mpl.cm.viridis, interpolation='none')
ax2.set_title('Halpha')
fig.colorbar(halphaplot, ax=ax2)

plt.show()

#hdr = fits.Header()
#hdr = getheader('velocity_map.fits')
#hduprim = fits.PrimaryHDU(data=data1,header=hdr)
#masked = fits.HDUList([hduprim])
#masked.writeto('masked_velmap.fits', overwrite=True)
