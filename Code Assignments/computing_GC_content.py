
import re
pattern= r">Rosalind"
file_path=  "file_name"
samp_sets= {}
current_id=""
with open(file_path, "r") as f:
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




        
         
