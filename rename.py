import re, os, glob

files = glob.glob('*.jpg')
n=0
for f in files:
    r=r"\s\(\d.*"
    name=re.sub(r, str(n)+'.jpg', f)
    os.rename(f, name)
    n+=1

