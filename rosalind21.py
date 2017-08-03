sequence_raw = raw_input('>')

sequence_forward = list(sequence_raw)
sequence_complement = []
match = []
list_index = []
length_string = []

for i in range(0,len(sequence_forward)):
	if sequence_forward[i] == 'T':
		sequence_complement.append('A')
	elif sequence_forward[i] == 'A':
		sequence_complement.append('T')
	elif sequence_forward[i] == 'G':
		sequence_complement.append('C')
	elif sequence_forward[i] == 'C':
		sequence_complement.append('G')
	else: 
		pass

		
# start with position 0 in forward and -1 in back. loop through 0,1,2 so forth while keeping -1
#then start over with position 0 and -2/
#continue until the complement strand hits 3 from the end because we are looking at palindromes > 4
		
def compare(forward,backward): #index of nucleotide position back and forth currently
	forward_log = sequence_forward[forward]
	reverse_log = sequence_complement[backward]
	
	if backward == -1 * len(sequence_forward):		# DO THIS PART. FIND POSITIONS OF THE THINGS. NEED INDICES OF DUPLICATES
		
	
		for i in match:
			
			duplicate(sequence_raw, i)
		
		for i in match:
			length_string.append(len(i))
		

				
	
	elif forward + abs(backward) == len(sequence_forward): # when we've checked all 0,1,... up to the complement position, 
															#we move along complement and start over on main strand
		backward -= 1 
		compare(0, backward)
	
	elif sequence_forward[forward] == sequence_complement[backward]: #if we hit match, start loop_check function
		forward += 1 #first index after match 
		loop_check(forward, backward) #include forward and backward to run compare again from 2nd function
	else:		#no match, move along main strand and run compare again
		forward += 1
		compare(forward, backward)

def loop_check(thing3, thing4):
	distance = len(sequence_forward) + thing4 - thing3 + 1 #number nucleotides between the bases. add one because indices start at 0
	

	crap = sequence_complement[thing4 - distance : thing4 ]
	jank = crap[::-1]
	
	
	if distance > 12 or distance < 3: #no longer than 12 nucleotide palindromes and no shorter than 4
		compare(thing3, thing4) #start compare function. thing3 is 1 further than original. thing4 is backward so wait to change this.
	
	
	elif sequence_forward[thing3 : thing3 + distance ] == jank: # check if segment between matches are equal
		
		match.append(''.join(sequence_forward[thing3 - 1 : thing3 + distance]) )#important part keep
		compare(thing3, thing4)
	
	else:
		compare(thing3, thing4)

def duplicate(string, item, offset=0):   # finds duplicate substrings and appends index to lists 
	i = string.find(item, offset)			# x separates indices where they appear. duplicates appear twice
	while i>= 0:
		list_index.append(i)
		i = string.find(item, i+1)
	list_index.append('x')

		
compare(0,-1)
print match
print length_string
print list_index
#TCAATGCATGCGGGTCTATATGCAT
		
		
		
