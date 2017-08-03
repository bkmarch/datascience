#match the first 3 nucleotides to the final 3.
open_file = open('c:\dir1\\rosalind12.txt')
raw_file = list(open_file)
raw_file = [i.replace("\n","") for i in raw_file] #removes \n in our opened file.
sequence_name = [i for i in raw_file if '>' in i] # sorts our file. puts items with a > in this list. without > in the next list.
sequence = [i for i in raw_file if '>' not in i]  
first3 = [] #stores first 3 nucleotides for each sequence
last3 =[] #stores last 3

match1 =[] #stores matching items here
match2 = []

k_length = raw_input('how many nucleotides do you want to match? ') #the k value we designate in the problem
k_1 = int(k_length)


for item in sequence: #creates 2 new lists with the first 3 and last 3 nucleotides
	first3.append(item[0:k_1])
	last3.append(item[-1 * k_1:])

	   #needs to match the the items in first3 to last3. if match then assign to new list. then check if its matched to itself


def match_fnc(k):

	while k != 5:
		for i in range(0,len(sequence)):				
			if first3[k] == last3[i] and sequence[k] != sequence[i]: #checks if first 3 nuc match last 3 and they are not the same sequence
				match1.append(sequence[k])
				match2.append(sequence[i])
			else:
				pass
		k += 1 #increments our k for the while function to eventually terminate. k=1 i=1,2,3,.. and then k=2 i=1,2,3, and so forth
	fnc_2()
	
def fnc_2(): 
	
	for i in range(0,len(match1)):
		index_in_sequence_name = sequence.index(match1[i]) #find index number in sequence list associated with the value in match 1
		match1[i] = sequence_name[index_in_sequence_name] #uses that index number to find our sequence name in sequence_name list
	
	for i in range(0,len(match2)):
		index_in_sequence_name = sequence.index(match2[i]) #same thing as above but with match 2 list
		match2[i] = sequence_name[index_in_sequence_name]
	fnc_3()
	
def fnc_3():
	for i in range(0,len(match1)):
		print "%s matches with %s" % (match1[i], match2[i])  #prints the pairing values in our 2 lists.
		
match_fnc(0)


