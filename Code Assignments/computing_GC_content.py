
import re
pattern= r">Rosalind"
file_path=  "/Users/jaeeraut/Downloads/rosalind_gc (1).txt"
samp_sets= {}
current_id=""
with open("/Users/jaeeraut/Downloads/rosalind_gc (1).txt", "r") as f:
    #fasta = f.read().strip()
    for line_num, line in enumerate(f,1):
        if re.search(pattern,line):
            current_id=(line.strip())
            samp_sets[current_id]=""
        else:
            samp_sets[current_id]+=(line.strip())


#making dictinary smap_perc to track GC/tot percentages
tot_nuc=0
samp_perc={}
for key in samp_sets:
    tot_nuc= len(samp_sets[key])
    tot_GC= samp_sets[key].count("G") + samp_sets[key].count("C")
    samp_perc[key]= tot_GC/tot_nuc
    


print(samp_perc)

#finding max percentages 
max_value= max(samp_perc.values())
max_key= max(samp_perc,key=samp_perc.get)

print(f'{max_key}: {max_value*100}%')

#print(f'The total amount of nucleotides is {tot_nuc} and total number of G or C is {tot_GC}')
#print(f"The percentage of GC is:" ((tot_GC/tot_nuc) * 100))


        
#make another dictaniary that stores the percent GC count from what i am currently using for each vlaue,
#  then i could in another for loop go trohugh which value is the biggest

         
