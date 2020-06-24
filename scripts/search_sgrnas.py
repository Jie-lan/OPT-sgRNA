import sys
sys.path.append("../scripts")
import Levenshtein
import onehot
import os
import math

class search:
	def get_complement(self,sequence):
		sequence = sequence.upper()
		sequence = sequence.replace('A', 't')
		sequence = sequence.replace('T', 'a')
		sequence = sequence.replace('C', 'g')
		sequence = sequence.replace('G', 'c')
		L=sequence[::-1]
		return L.upper()
	
	def load_file(self,path):
		seq={}
		t=[]
		for f in open(path,'r'):
			f=f.strip()
			if '>' not in f:
				seq[t[-1]]['+']+=f
			else:
				seq[f]={}
				seq[f]['+']=''
				t.append(f)
		for k in seq.keys():			
			seq[k]['-']=self.get_complement(seq[k]['+'])
		
		return seq
			
	def distance(self,str1,str2):
		dis={}
		d=Levenshtein.distance(str1,str2)
		if d<=4 and d>=1:
			if d not in dis.keys():
				dis[d]=1
			else:
				dis[d]+=1
		return dis
		
	def search(self,query,pam):
		seq=self.load_file(query)
		sgrnas={}
		for k in seq.keys():
			sgrnas[k]=[]
			for k1 in seq[k].keys():
				if pam=='NGG':
					sg=[]
					for i in range(len(seq[k][k1])-23):
						if seq[k][k1][i:i+23].endswith('GG') and 'N' not in seq[k][k1][i:i+23]:
							if seq[k][k1][i:i+23] not in sg:
								sg.append(seq[k][k1][i:i+23])
								sgrnas[k].append(seq[k][k1][i:i+20]+':'+k1+':'+seq[k][k1][i+20:i+23]+':'+str(i)+':'+str(i+23))
		
		return sgrnas

	def off_target(self,sgrna,pam,opt):
		ref_seq=self.load_file(opt)
		sgrna=sgrna.split(':')
		for k in ref_seq.keys():
			if pam=='NGG':
				for i in range(len(ref_seq['+'])-23):
					if ref_seq[k][i:i+23].endswith('GG'):
						diff=self.distance(sgrna[0]+sgrna[2],ref_seq[k][i:i+23])
						if len(diff.keys())>0:
							return diff
						else:
							return '0'
		 
	
	def score(self,sgrna,rules):
		
		s=0
		sgrna=sgrna.split(':')
		#ftemp=open('temp.txt','w')
		#ftemp.writelines(sgrna[0]+'\n')
		#ftemp.close()
		#str1=os.popen("RNAfold -p -d2 --noLP temp.txt|grep 'kcal'|awk '{print $6}'").read()
		#str2=str1.split('\n')
			
		#seq2onehot=[float(str2[0])]+onehot.onehot(sgrna[0][::-1])
		
		seq2onehot=onehot.onehot(sgrna[0][::-1])
		s+=float(rules[0])
		for i in range(len(seq2onehot)):
			s+=int(seq2onehot[i])*float(rules[i+1])
		
		scores=1/(1+math.exp(-s))	
			
		return sgrna[0]+sgrna[2]+':'+sgrna[1]+':'+str(scores)
