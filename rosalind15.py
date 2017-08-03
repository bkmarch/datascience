from decimal import *
from math import factorial

number_AaBb = int(raw_input('Number of AaBb Organisms: '))
k_generation = int(raw_input('generation number: '))


total_k_gen = 2 ** (k_generation) #number of offspring in the k generation

#separate into 3 domains - each for one parent's genotype (other parent is always hetero genotype) 

#we know the distribution of parent first gen offspring

parents = 1


#heterozygous in next offspring
def offspring(dom, het, rec, current_gen_k):
	
	while k_generation != current_gen_k:  
		dom_het = dom * 0.5
		het_het = het * 0.5
		rec_het = rec * 0.5

		#probability dominant offspring
		dom_dom = dom * 0.5
		het_dom = het * 0.25

		#probability recessive offspring
		het_rec = het * 0.25
		rec_rec = rec * 0.5
		
		current_gen_k += 1
		dom = dom_dom + het_dom
		het = dom_het + het_het + rec_het
		rec = het_rec + rec_rec
		offspring(dom, het, rec, current_gen_k)
		
	else: #need to solve for probability of at least 1 or at least 2 etc...
		running_probability = 0
		het = (het ** 2) # to solve two both for A and B together
		for i in range(number_AaBb, total_k_gen + 1):
			running_probability += (factorial(total_k_gen) * (het ** i) * ((1-het) ** (total_k_gen - i))) / ((factorial(i) ) * factorial((total_k_gen - i)))
	
		print running_probability
		
		
		
		


	
		
	
offspring(0.25, 0.5, 0.25, 1)

