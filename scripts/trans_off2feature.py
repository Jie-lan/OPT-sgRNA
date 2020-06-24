from collections import Counter
import math

param={'1-2':-1.03,'3-8':-1.52,'9-15':-1.18,'16-18':-0.90,'19-20':-0.87}
#find idx of mismatch
def mis_idx(str1,str2):
	idx=[]
	for i in range(20):
		if str1[i]==str2[i]:
			continue
		else:
			idx.append(i)
	return idx

sg2off={}
def off_score(sg,off):
	idx=mis_idx(sg,off)
		
	feature=[]
	for i in idx:
		if i+1 in range(1,3):
			feature.append('19-20')
		elif i+1 in range(3,6):
			feature.append('16-18')
		elif i+1 in range(6,13):
			feature.append('9-15')
		elif i+1 in range(13,19):
			feature.append('3-8')
		else:
			feature.append('1-2')
	count=Counter(feature)
	K=['1-2','3-8','9-15','16-18','19-20']
	for k in K:
		if k not in count.keys():
			count[k]=0
	score=0
	for k in count.keys():
		score+=count[k]*param[k]	
	return math.exp(score)
#print(off_score('ATGCATGCATGCATGCATCG','ATGCATGCATGCATGCATCC'))
