'''
This script generates an overlap graph given a collection of k-mers, outputs as an adjacency list
'''


file = open("/Users/ashle/Downloads/rosalind_ba3c.txt")

seqs = []

#add seqs from file to list
for line in file:
    seqs.append(line.strip("\n"))


#seqs = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT",]

#get k from len of first seq
k = len(seqs[0])

#initialize empty list
adj_list = []


#iterate through seqs list by position
for i in range(len(seqs)):
    seq1 = seqs[i]
    #iterate through again
    for j in range(len(seqs)):
        seq2 = seqs[j]
        #if positions are different
        if i != j:
            #if suffix of seq1 = prefix of seq2, add to adjacency list
            if seq1[1:k] == seq2[0:k-1]:
                adj_list.append(seq1 + " -> " + seq2)


output = open("/Users/ashle/OneDrive/BIOI 500/rosalind/rosalind6_answer.txt", "w")

#output list to file
for item in adj_list:
    output.write(item + "\n")

