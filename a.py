import glob, datetime, os

files = glob.glob('./images/university-logos/*')

for f in files:
	os.rename(f,f[:-1])