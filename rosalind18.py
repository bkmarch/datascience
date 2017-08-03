dna_forward = raw_input('>')

dna_f_list = list(dna_forward)
dna_r_list = [] # reverse complement strand

rna_f_list = []
rna_r_list = []

for i in reversed(dna_f_list):  #used reversed DNA for complement
	if i == 'A':
		dna_r_list.append('T')
	elif i == 'T':
		dna_r_list.append('A')
	elif i == 'C':
		dna_r_list.append('G')
	elif i == 'G':
		dna_r_list.append('C')
	else:
		break

#translation process
for i in dna_f_list:
	if i == 'A':
		rna_f_list.append('U')
	elif i == 'T':
		rna_f_list.append('A')
	elif i == 'C':
		rna_f_list.append('G')
	elif i == 'G':
		rna_f_list.append('C')
	else:
		break
		
for i in dna_r_list:
	if i == 'A':
		rna_r_list.append('U')
	elif i == 'T':
		rna_r_list.append('A')
	elif i == 'C':
		rna_r_list.append('G')
	elif i == 'G':
		rna_r_list.append('C')
	else:
		break

index_position_start_f = []
index_position_start_r = []
		
#find start codon positions in our rna lists
for i in range(0,len(rna_f_list)-2):
	if rna_f_list[i] == 'A' and rna_f_list[i+1] == 'U' and rna_f_list[i+2] == 'G':
		index_position_start_f.append(i)

for i in range(0,len(rna_r_list)-2):
	if rna_r_list[i] == 'A' and rna_r_list[i+1] == 'U' and rna_r_list[i+2] == 'G':
		index_position_start_r.append(i)

print index_position_start_f
print index_position_start_r

#need to do: translate the rna from start to stop positions. 


