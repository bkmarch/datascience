#find substring and delete it from another string
#then transcribe bt finding start and stop codon
#return protein chain



sequence = raw_input('main sequence:')
intron_list = []
length_intron = []
mRNA = []

def intron_input():
	prompt_intron = raw_input('Another Intron Sequence Y/N:')

	if prompt_intron == 'Y':   #prompts for the intron sequence and then asks if we have another intron sequence
		new_intron = raw_input('>')
		intron_list.append(new_intron)
		intron_input()

	elif prompt_intron == 'N': #start new program if we have no more introns
		
		rna_splice()

	else:
		print "I don't understand that command"
		intron_input()

def rna_splice(): #remove introns using simple .replace() function
	sequence2 = sequence
	for i in intron_list:
		sequence2 = sequence.replace(i,"")
	
	transcription(sequence2)
	
def transcription(fart):
	
	for i in fart: #transcription
		if i == "T":
			mRNA.append("A")
		if i == "A":
			mRNA.append("U")
		if i == "C":
			mRNA.append("G")
		if i == "G":
			mRNA.append("C")
	start_stop()
			
def start_stop():	
	
	start_codon = 0
	stop_codon = 0
	for i in range(0,len(mRNA)-2): #find start and stop codon positions
		if start_codon != 0 and stop_codon != 0:
			translation()
			break
		elif mRNA[i] == "A" and mRNA[i+1] == "U" and mRNA[i+2] == "G":
			start_codon = i
			del mRNA[0:start_codon]
		elif mRNA[i] == "U" and mRNA[i+1] == "G" and mRNA[i+2] == "A":
			stop_codon = i+2
			del mRNA[stop_codon:]
		elif mRNA[i] == "U" and mRNA[i+1] == "A" and mRNA[i+2] == "A":
			stop_codon = i+2
			del mRNA[stop_codon:]
		elif mRNA[i] == "U" and mRNA[i+1] == "A" and mRNA[i+2] == "G":
			stop_codon = i+3
			del mRNA[stop_codon:]
			
		else:
			pass

	

def translation():
	
	mRNA_codon = [i+j+k for i,j,k in zip((mRNA[::3]), mRNA[1::3], mRNA[2::3])] # slices into 3codon pieces
	
	
	print mRNA_codon
		

#last part is just translating 

intron_input()

