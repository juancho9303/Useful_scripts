import pyregion
region_name = "ds9.reg"
r = pyregion.open(region_name)
print r[1]
