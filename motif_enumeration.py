import itertools

#open file with data
file = open("/Users/ashle/Downloads/rosalind_ba2a.txt", "r")
#create file for output
output = open("/Users/ashle/OneDrive/BIOI 500/rosalind/rosalind3_answer.txt", "w")

#extarct data from file
line_list = []
for line in file:
    line_list.append(line.strip())

kd = line_list[0]
kd_list = kd.split(" ")
k = int(kd_list[0])
d = int(kd_list[1])
dna = line_list[1:]


#k = 3
#d = 1
#dna = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]


#function to generate all possible kmers for any value of k, outputs a list
def all_possible_kmers(k):
    all_kmers = []
    bases = ["A", "T", "C", "G"]
    all_list = list(itertools.product(bases, repeat=k))
    for kmer in all_list:
        km = "".join(kmer)
        all_kmers.append(km)
    return all_kmers
    

#function to get all kmers from a sequence, outputs a list
def get_kmers(seq, k):
    kmers = []
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        kmers.append(kmer)
    return kmers

#function to generate hamming distance
def get_hamm_dist(seq1, seq2):
    hamm_dist = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            hamm_dist += 1
    return hamm_dist


#function to get all kd motifs, outputs a set
def motif_enum(dna, k, d):
    #list to keep track of sets of possible motifs from each seq
    poss_kd_motifs_all_seq = []
    #get all possible kmers based on value of k
    all_kmers = all_possible_kmers(k)
    #get all kdmers for each seq, store in a list of sets
    for seq in dna:
        poss_kd_motifs = []
        kmers = get_kmers(seq, k)
        for i in range(len(kmers)):
            for j in range(len(all_kmers)):
                if get_hamm_dist(kmers[i],all_kmers[j]) <= d:
                    poss_kd_motifs.append(all_kmers[j])
        #add set of possible kd motifs from seq to list
        poss_kd_motifs_all_seq.append(set(poss_kd_motifs))

    #extract first set from list
    kd_motifs = poss_kd_motifs_all_seq[0]
    #take the intersection of all sets to get kd motifs common across all seqs
    for i in range(1, len(poss_kd_motifs_all_seq)):
        kd_motifs = kd_motifs.intersection(poss_kd_motifs_all_seq[i])        

    return list(kd_motifs)
                
kd_motifs = motif_enum(dna, k, d)


#write answer to file
answer = ""
for motif in kd_motifs:
    answer = answer + motif + " "

output.write(answer)






