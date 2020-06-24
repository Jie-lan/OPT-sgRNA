import sys
sys.path.append("./scripts")
import argparse
from search_sgrnas import *
a=search()
def main():
	optargv = argparse.ArgumentParser()
	sub_parser = optargv.add_subparsers(title='subcommands',description='valid subcommands',help='config subscommand help')
		
	#subcommands off_target
	off_target_parser = sub_parser.add_parser('off_target',help='search off-target sites based reference genome/sequence')
	off_target_parser.add_argument('--sgrna',help='reference genome/sequence path',required=True)
	off_target_parser.add_argument('--ref',help='reference genome/sequence path',required=True)
	off_target_parser.add_argument('--pam',help='PAM',required=True)
	off_target_parser.add_argument('--out',help='out file',required=False)
	off_target_parser.set_defaults(func=off_target)
	#subcommands search
	search_parser = sub_parser.add_parser('search',help='search sgRNA based on your fasta and PAM')
	search_parser.add_argument('--query',help='fasta file',required=True)
	search_parser.add_argument('--pam',help='PAM',required=True)
	search_parser.add_argument('--ref',help='reference genome/sequence path or name',required=False)
	search_parser.add_argument('--out',help='out file',required=True)
	search_parser.set_defaults(func=search)
	#subcommmands score
	score_parser = sub_parser.add_parser('score',help='fetch sgRNAs\' score')
	score_parser.add_argument('--path',help='reference genome/sequence path')
	score_parser.add_argument('--seq',help='sgRNA sequence')
	score_parser.add_argument('--pam',help='PAM')
	score_parser.add_argument('--out',help='out file')
	score_parser.set_defaults(func=score)
	
	args=optargv.parse_args()	
	args.func(args)
#rules
rules=[]

for r in open('./sgRNA_library/weight.txt','r'):
	r=r.strip()
	r=r.split('\t')
	rules.append(r[1])	
#print('weight loading')

def write_file(dic,path):
	#print(path)
	fout=open(path,'w')
	#print(fout)
	if isinstance(dic,dict):
		#print('Yes, dic is a dictionary!')
		for k in dic.keys():
			for k1 in dic[k]:
				k1=k1.split(':')
				fout.writelines(k1[0]+k1[2]+'\t'+k1[1]+'\t'+k+'\t'+k1[3]+'-'+k1[4]+'\n')
	else:
		#print('NO, dic is not a dictionary!')
		gi=[]
		for s in dic:
			s=s.split(':')
	
			if s[3] not in gi:
				gi.append(s[3])
				fout.writelines(s[0]+'\t'+s[1]+'\t'+s[2]+'\n')
			else:
				fout.writelines(s[0]+'\t'+s[1]+'\t'+s[2]+'\n')
	fout.close()
	
def off_target(args):
	print(a.off_target(args.out,args.pam,args.sgrna))

def search(args):
	dic=a.search(args.query,args.pam)
	#print(args.out)
	try:
		write_file(dic,args.out)
		print('\n\nSearching for sgRNAs finished.\n')
	except:
		print('Write failed')
def score(args):
	#sgrnas=a.search(args.path,args.pam)	
	print(a.score(args.seq,rules))	
	#Score=[]
	#dic=[]
	#for gi in sgrnas.keys():
	#	for sgrna in sgrnas[gi]:
	#		Score.append(a.score(sgrna,rules))
	
	#	sg2score={}
	#	for k in Score:
	#		k=k.split(':')
	#		sg2score[k[0]+':'+k[1]]=k[2]
	#	newdic=sorted(sg2score.items(),key=lambda d:d[1],reverse=True)
		
	
	#	for v in newdic:
	#		if float(v[1])>0.0:
			
	#			dic.append(v[0]+':'+v[1]+':'+gi)
	
	#	write_file(dic,args.out)
	#print 'sgRNAs-scoring finished.\n'
if __name__=="__main__":
	main()
