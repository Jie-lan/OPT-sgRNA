from collections import Counter
from trans_off2feature import off_score 
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("file1",help="filename you want to input")
parser.add_argument("file2",help="filename you want to output")
parser.add_argument("file3",help="filename you want to output")
parser.add_argument("N",help="Number of off-target sites")
parser.add_argument('O',help="Number of sgRNA by activity")
args=parser.parse_args()

f2=open(args.file2,"a")
f3=open(args.file3,"a")

sg2off_exon={}
sg2off_prom={}
t=0
with open(args.file1,'r') as f1:
	next(f1)
	for f in f1:
		f=f.strip()
		f=f.split('\t')
		sg=f[3].split(':')
		off=f[0].split(':')
		
		if '_up_2000_' in f[0]:
			t+=1
			if f[3]+':'+f[4] not in sg2off_prom.keys():
				sg2off_prom[f[3]+':'+f[4]]=[]
				sg2off_prom[f[3]+':'+f[4]].append(f[0]+':'+f[1]+':'+f[2])
			else:
				sg2off_prom[f[3]+':'+f[4]].append(f[0]+':'+f[1]+':'+f[2])
		else:
			if f[3]+':'+f[4] not in sg2off_exon.keys():
				sg2off_exon[f[3]+':'+f[4]]=[]
				sg2off_exon[f[3]+':'+f[4]].append(f[0]+':'+f[1]+':'+f[2])
			else:
				sg2off_exon[f[3]+':'+f[4]].append(f[0]+':'+f[1]+':'+f[2])

sgRNA_prom=set()
for k in sg2off_prom.keys():
	k1=k.split(':')
	sgRNA_prom.add(k1[-1])

sg2off_sum={}
sg2off_gene={}
for k in sg2off_exon.keys():
	k1=k.split(':')
	off_scores=0.0
	if k1[-1] not in sgRNA_prom:
		f2.writelines(k+'\t')
		i=len(sg2off_exon[k])
		v_uniq=set()
		for v in sg2off_exon[k]:
			v=v.split(':')
			
			if k1[1] == v[1]:
				i-=1
			else:	
				#print(k1[1],v[1],v[-1],k1[-1])
				off_scores+=off_score(v[-1],k1[-1])
				v_uniq.add(v[1])
		f2.writelines('\t'+str(i))
		if len(v_uniq)>0:
			sg2off_gene[k]=list(v_uniq)
		for v_u in v_uniq:
			f2.writelines('\t'+v_u)
		f2.writelines('\n')
	sg2off_sum[k]=off_scores
	
di=sorted(sg2off_sum.items(),key=lambda d:d[1], reverse = False)
d2={}
for d in di[:int(args.N)]:	
	k=d[0].split(':')
	score=os.popen('python /home/lanjie/sgRNA/app/scripts/sgdesign.py score --seq '+k[len(k)-1][:20]+':'+k[len(k)-3]+':'+k[len(k)-2]).read()
	score=score.strip()
	score=score.split(':')
	d2[d[0]+':'+str(d[1])]=score[-1]

	
d3=sorted(d2.items(),key=lambda d:d[1],reverse=True)
#f3.writelines('Gene\tEnsembl_gene_id\tEnsembl_exon_id\tExon_loci\tsgRNAloci(exon)\tsgRNA_strand\tsgRNA\toff-site\tActivity\n')
no_re=set()
for d in d3[:int(args.O)]:
	#print(d)
	koff=d[0].split(':0')
	k=d[0].split(':')
	if k[-2]+k[-3] not in no_re:
		#f3.writelines(k[1]+'\t'+k[2]+'\t'+k[0]+'\t'+k[3]+'('+k[6]+')'+':'+k[4]+'-'+k[5]+'\t'+k[7]+'\t'+k[8]+'\t'+k[10]+k[9]+'\t'+k[11]+'\t')
		f3.writelines(k[0]+'\t'+k[2]+'\t'+k[3]+'\t'+k[5]+k[4]+'\t'+k[6]+'\t')
		no_re.add(k[-2]+k[-3])	
		try:
			for j in range(len(sg2off_gene[koff[0]])-1):
			
				f3.writelines(sg2off_gene[koff[0]][j]+',')
			f3.writelines(sg2off_gene[koff[0]][len(sg2off_gene[koff[0]])-1]+'\t')
		except KeyError:
			f3.writelines('Non off-target genes\t')
		f3.writelines(str(d[1])+'\n')

f1.close()
f2.close()
f3.close()
