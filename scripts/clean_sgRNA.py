import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file1",help="filename you want to input")
parser.add_argument("file2",help="filename you want to output")
args=parser.parse_args()

f1=open(args.file1,"r")
f2=open(args.file2,"w")

sg=set()
ids=[]
for f in f1:
	f=f.strip()
	if '>' in f:
		ids.append(f)
	else:
		if 'TTTT' not in f and f[:20].count('G')+f[:20].count('C')>=8:
			if f not in sg:
				f2.writelines(ids[-1]+'\n'+f+'\n')
				sg.add(f)

f1.close()
f2.close()


