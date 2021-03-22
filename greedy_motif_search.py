

#open file with data
file = open("/Users/ashle/Downloads/rosalind_ba2d.txt", "r")

#extarct data from file
line_list = []
for line in file:
    line_list.append(line.strip())

kt = line_list[0]
kt_list = kt.split(" ")
k = int(kt_list[0])
t = int(kt_list[1])
dna = line_list[1:]




#function to get all kmers from a sequence, outputs a list
def get_kmers(seq, k):
    kmers = []
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        kmers.append(kmer)
    return kmers

#function to get the first kmer from a sequence
def get_first_kmer(seq, k):
    kmer = seq[0:k]
    return kmer


#function to get the profile for a list of motifs
def get_profile(motifs_list, k, t):
    #profile is a dict, key is base, value is list of ratios
    profile = {"A":[], "C":[], "G":[], "T":[]}
    a_ratio_list = []
    c_ratio_list = []
    g_ratio_list = []
    t_ratio_list = []
    #go through motifs by index
    for i in range(k):
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        #At a given index count bases across all motifs
        for motif in motifs_list:
            base = motif[i]
            if base == "A":
                a_count += 1
            if base == "C":
                c_count += 1
            if base == "G":
                g_count += 1
            if base == "T":
                t_count += 1
        #calculate ratio of each base at given index and add to list
        a_ratio = round(a_count/t, 2)
        c_ratio = round(c_count/t, 2)
        g_ratio = round(g_count/t, 2)
        t_ratio = round(t_count/t, 2)
        a_ratio_list.append(a_ratio)
        c_ratio_list.append(c_ratio)
        g_ratio_list.append(g_ratio)
        t_ratio_list.append(t_ratio)
    #add ratio lists to profile
    profile["A"] = a_ratio_list
    profile["C"] = c_ratio_list
    profile["G"] = g_ratio_list
    profile["T"] = t_ratio_list
    return profile


#use the profile to get the probability for a possible motif
def get_prob(profile, poss_motif, k):
    prob = 1
    #iterate through indices of possible motif and multiply probability ratios to sum based on base match
    for i in range(k):
        if poss_motif[i] == "A":
            a_ratio_list = profile["A"]
            ratio = a_ratio_list[i]
            prob = float(prob*ratio)
        if poss_motif[i] == "C":
            c_ratio_list = profile["C"]
            ratio = c_ratio_list[i]
            prob = float(prob*ratio)
        if poss_motif[i] == "G":
            g_ratio_list = profile["G"]
            ratio = g_ratio_list[i]
            prob = float(prob*ratio)
        if poss_motif[i] == "T":
            t_ratio_list = profile["T"]
            ratio = t_ratio_list[i]
            prob = float(prob*ratio)
    return prob
  

#function to get score of motifs list
def get_score(motifs_list, k, t):
    score = 0
    a_count_list = []
    c_count_list = []
    g_count_list = []
    t_count_list = []
    for i in range(k):
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        #At a given index count bases across all motifs
        for motif in motifs_list:
            base = motif[i]
            if base == "A":
                a_count += 1
            if base == "C":
                c_count += 1
            if base == "G":
                g_count += 1
            if base == "T":
                t_count += 1
        a_count_list.append(a_count)
        c_count_list.append(c_count)
        g_count_list.append(g_count)
        t_count_list.append(t_count)
    #find max count at each index, subtract from t and add all together to get score    
    for i in range(k):
        m = max(a_count_list[i],c_count_list[i],g_count_list[i],t_count_list[i])
        score = score + (t-m)
    return score


def greedy_motif_search(dna, k, t):
    best_motifs_list = []
    #create initial best motif list with first kmer from each seq in dna
    for seq in dna:
        first_kmer = get_first_kmer(seq, k)
        best_motifs_list.append(first_kmer)

    #get list of all kmers for first seq and iterate through
    seq1_kmers = get_kmers(dna[0], k)
    for kmer in seq1_kmers:
        motif1 = kmer
        #initialize motifs list with kmer from first seq
        motifs_list = [motif1]
        #start with list of 1
        #use profile to determine kmer that is most probable motif in next seq
        #then add most probable motif to motif list
        #continue adding to motif list until it has a motif for each seq in dna
        for i in range(1,t):
            #get profile for motifs list (i = number of motifs in list)
            profile = get_profile(motifs_list, k, i)
            #get kmers for next seq in dna
            all_kmers_current_dna = get_kmers(dna[i], k)
            #set first possible motif to first kmer
            motif_for_current_dna = get_first_kmer(dna[i], k)
            #iterate through all kmers and compare probabilities
            for kmer_current in all_kmers_current_dna:
                #get probabilities of new and current
                prob_new = get_prob(profile, kmer_current, k)
                prob_current_motif = get_prob(profile, motif_for_current_dna, k)
                #replace current motif with new if prob of new is greater
                if prob_new > prob_current_motif:
                    motif_for_current_dna = kmer_current
            #add most probable motif to motifs list
            motifs_list.append(motif_for_current_dna)
        #replace best motif list with current motifs list if current has a lower score
        if get_score(motifs_list, k, t) < get_score(best_motifs_list, k, t):
            best_motifs_list = motifs_list
    
    return best_motifs_list


motif_list = greedy_motif_search(dna, k, t)

for motif in motif_list:
    print(motif)






