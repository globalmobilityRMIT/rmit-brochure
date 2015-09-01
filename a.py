import glob, datetime, os

files = glob.glob('./images/universities/*')

for f in files:
	os.rename(f,f[:-4]+f[-3:])