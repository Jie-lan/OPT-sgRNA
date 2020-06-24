import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file1",help="filename you want to input")
parser.add_argument("file2",help="filename you want to output")
args=parser.parse_args()

f1=open(args.file1,"r")
f2=open(args.file2,"w")
print(f1)
sg=set()

for f in f1:
	f=f.strip()
	f=f.split('\t')
	n=f[2].split(' ')
	print(n[0])
	m=n[0].split('>')
	print(m[0])
	if 'TTTT' not in f[0] and f[0][:20].count('G')+f[0][:20].count('C')>=8:
		if f[0] not in sg:
			f2.writelines(n[0]+':'+n[1]+':'+f[3]+':'+f[1]+':'+f[0][20:]+'\n'+f[0][:20]+'\n')
			sg.add(f[0])
f1.close()
f2.close()


