### one-hot transferring
def onehot(sgRNA):
	seq_onehot=[]
	if sgRNA.count('G')+sgRNA.count('C')>=14:
		seq_onehot.append(1)
	else:
		seq_onehot.append(0)
	for j in range(len(sgRNA)):
		if sgRNA[j]=='A':
			for a in list('1000'):
				seq_onehot.append(int(a))
		elif sgRNA[j]=='T':
			for a in list('0100'):
                                seq_onehot.append(int(a))
		elif sgRNA[j]=='G':
			for a in list('0010'):
                                seq_onehot.append(int(a))
		elif sgRNA[j]=='C':
			for a in list('0001'):
                                seq_onehot.append(int(a))
	for k in range(len(sgRNA)-1):
		if 'AA' in sgRNA[k:k+2]:
			for a in list('1000000000000000'):
				seq_onehot.append(int(a))
		elif 'AT' in sgRNA[k:k+2]:
			for a in list('0100000000000000'):
				seq_onehot.append(int(a))
		elif 'AG' in sgRNA[k:k+2]:
                        for a in list('0010000000000000'):
                                seq_onehot.append(int(a))
		elif 'AC' in sgRNA[k:k+2]:
                        for a in list('0001000000000000'):
                                seq_onehot.append(int(a))
		elif 'TA' in sgRNA[k:k+2]:
                        for a in list('0000100000000000'):
                                seq_onehot.append(int(a))
		elif 'TT' in sgRNA[k:k+2]:
                        for a in list('0000010000000000'):
                                seq_onehot.append(int(a))
		elif 'TC' in sgRNA[k:k+2]:
                        for a in list('0000001000000000'):
                                seq_onehot.append(int(a))
		elif 'TG' in sgRNA[k:k+2]:
                        for a in list('0000000100000000'):
                                seq_onehot.append(int(a)) 
		elif 'CA' in sgRNA[k:k+2]:
                        for a in list('0000000010000000'):
                                seq_onehot.append(int(a)) 
		elif 'CT' in sgRNA[k:k+2]:
                        for a in list('0000000001000000'):
                                seq_onehot.append(int(a))
		elif 'CC' in sgRNA[k:k+2]:
                        for a in list('0000000000100000'):
                                seq_onehot.append(int(a))
		elif 'CG' in sgRNA[k:k+2]:
                        for a in list('0000000000010000'):
                                seq_onehot.append(int(a))
		elif 'GA' in sgRNA[k:k+2]:
                        for a in list('0000000000001000'):
                                seq_onehot.append(int(a))
		elif 'GT' in sgRNA[k:k+2]:
                        for a in list('0000000000000100'):
                                seq_onehot.append(int(a))
		elif 'GC' in sgRNA[k:k+2]:
                        for a in list('0000000000000010'):
                                seq_onehot.append(int(a))
		elif 'GG' in sgRNA[k:k+2]:
                        for a in list('0000000000000001'):
                                seq_onehot.append(int(a))
	for k in range(len(sgRNA)-2):
		rna=sgRNA
		if 'AAA' in rna[k:k+3]:
			for a in list('1000000000000000000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'AAT' in rna[k:k+3]:
			for a in list('0100000000000000000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'AAC' in rna[k:k+3]:
			for a in list('0010000000000000000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'AAG' in rna[k:k+3]:
			for a in list('0001000000000000000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'ATA' in rna[k:k+3]:
			for a in list('0000100000000000000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'ATT' in rna[k:k+3]:
			for a in list('0000010000000000000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'ATG' in rna[k:k+3]:
			for a in list('0000001000000000000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'ATC' in rna[k:k+3]:
			for a in list('0000000100000000000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'AGA' in rna[k:k+3]:
			for a in list('0000000010000000000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'AGT' in rna[k:k+3]:
			for a in list('0000000001000000000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'AGG' in rna[k:k+3]:
			for a in list('0000000000100000000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'AGC' in rna[k:k+3]:
			for a in list('0000000000010000000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'ACA' in rna[k:k+3]:
			for a in list('0000000000001000000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'ACT' in rna[k:k+3]:
			for a in list('0000000000000100000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'ACG' in rna[k:k+3]:
			for a in list('0000000000000010000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'ACC' in rna[k:k+3]:
			for a in list('0000000000000001000000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TAA' in rna[k:k+3]:
			for a in list('0000000000000000100000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TAT' in rna[k:k+3]:
			for a in list('0000000000000000010000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TAG' in rna[k:k+3]:
			for a in list('0000000000000000001000000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TAC' in rna[k:k+3]:
			for a in list('0000000000000000000100000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TTA' in rna[k:k+3]:
			for a in list('0000000000000000000010000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TTT' in rna[k:k+3]:
			for a in list('0000000000000000000001000000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TTG' in rna[k:k+3]:
			for a in list('0000000000000000000000100000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TTC' in rna[k:k+3]:
			for a in list('0000000000000000000000010000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TGA' in rna[k:k+3]:
			for a in list('0000000000000000000000001000000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TGT' in rna[k:k+3]:
			for a in list('0000000000000000000000000100000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TGG' in rna[k:k+3]:
			for a in list('0000000000000000000000000010000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TGC' in rna[k:k+3]:
			for a in list('0000000000000000000000000001000000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TCA' in rna[k:k+3]:
			for a in list('0000000000000000000000000000100000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TCT' in rna[k:k+3]:
			for a in list('0000000000000000000000000000010000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TCG' in rna[k:k+3]:
			for a in list('0000000000000000000000000000001000000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'TCC' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000100000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GAA' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000010000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GAT' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000001000000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GAG' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000100000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GAC' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000010000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GTA' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000001000000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GTT' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000100000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GTG' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000010000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GTC' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000001000000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GGA' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000100000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GGT' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000010000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GGG' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000001000000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GGC' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000100000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GCA' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000010000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GCT' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000001000000000000000000'):
				seq_onehot.append(int(a))
		elif 'GCG' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000100000000000000000'):
				seq_onehot.append(int(a))
		elif 'GCC' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000010000000000000000'):
				seq_onehot.append(int(a))
		elif 'CAA' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000001000000000000000'):
				seq_onehot.append(int(a))
		elif 'CAT' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000100000000000000'):
				seq_onehot.append(int(a))
		elif 'CAG' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000010000000000000'):
				seq_onehot.append(int(a))
		elif 'CAC' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000001000000000000'):
				seq_onehot.append(int(a))
		elif 'CTA' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000000100000000000'):
				seq_onehot.append(int(a))
		elif 'CTT' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000000010000000000'):
				seq_onehot.append(int(a))
		elif 'CTG' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000000001000000000'):
				seq_onehot.append(int(a))
		elif 'CTC' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000000000100000000'):
				seq_onehot.append(int(a))
		elif 'CGA' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000000000010000000'):
				seq_onehot.append(int(a))
		elif 'CGT' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000000000001000000'):
				seq_onehot.append(int(a))
		elif 'CGG' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000000000000100000'):
				seq_onehot.append(int(a))
		elif 'CGC' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000000000000010000'):
				seq_onehot.append(int(a))
		elif 'CCA' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000000000000001000'):
				seq_onehot.append(int(a))
		elif 'CCT' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000000000000000100'):
				seq_onehot.append(int(a))
		elif 'CCG' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000000000000000010'):
				seq_onehot.append(int(a))
		elif 'CCC' in rna[k:k+3]:
			for a in list('0000000000000000000000000000000000000000000000000000000000000001'):
				seq_onehot.append(int(a))
			
	return seq_onehot
