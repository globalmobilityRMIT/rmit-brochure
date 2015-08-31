import glob, datetime, os

files = glob.glob('./images/sliders/*')

for f in files:
	os.rename(f,f[:-3]+"."+f[-3:])