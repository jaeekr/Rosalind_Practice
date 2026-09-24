# input string 
def try1(samp):
    string= samp
    a_count= 0
    c_count= 0
    g_count= 0
    t_count= 0

    # checking for letter in string
    for i in string:

        if i == "A" :
            a_count += 1 

        elif i == "C":
            c_count += 1

        if i == "G":
            g_count += 1

        if i == "T":
            t_count+= 1
    return a_count, c_count, g_count, t_count


def try2(samp):
    nucs= {'a':0,'c':0,'g':0,'t':0}

    for i in samp:
        if i in nucs:
            nucs[i]+=1
    return nucs



