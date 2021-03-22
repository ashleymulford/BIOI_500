'''
This script performs genome assembly of DNA seqeucnces that form a cyclical de bruijn graph at some value k. Must consider all sequences provided and their reverse complements
The value of K is not provided. Outputs a cyclic superstring containing every read or its reverse complement.
'''

#import biopython classes
from Bio.Seq import Seq
from Bio import SeqIO

#open file
file = open("/Users/ashle/Downloads/rosalind_gasm.txt")

#add reads to list
reads_list = []
for line in file:
    #remove new line chars
    seq = line.rstrip("\n")
    #convert from str to seq type
    seq = Seq(seq)
    reads_list.append(seq)

#get reverse complement and add as str type to new list
all_reads_list = []
for seq in reads_list:
    reverse = str(seq.reverse_complement())
    all_reads_list.append(reverse)

#add original reads as str types
for seq in reads_list:
    seq = str(seq)
    all_reads_list.append(seq)

all_reads_set = set(all_reads_list)
all_reads_list = list(all_reads_set)

#function to get kmers given list of read and value of k
def get_kmer(read_list, k):
    kmer_list = []
    for seq in read_list:
        for i in range(len(seq)):
            for j in range(len(seq)+1):
                if j-i==k:
                    kmer = seq[i:j]
                    kmer_list.append(kmer)
    return kmer_list


#function to get k-1mers from kmers
def get_k1mers(kmer_list):
    pairs_list = []
    for kmer in kmer_set:
        length = len(kmer)
        left = kmer[0:length-1]
        right = kmer[1:length]
        pair = (left, right)
        pairs_list.append(pair)
    return pairs_list

for i in reversed(range(3, len(reads_list[0])+1)):
    kmer_list = get_kmer(all_reads_list, i)
    #convert to set
    kmer_set = set(kmer_list)
    #convert to list
    kmer_list = list(kmer_set)

    #get left and right k-1-mers and print
    k1mer_list = get_k1mers(kmer_list)

    #Go through kmers to look for two cycles
    len_list=len(k1mer_list)
    pair = k1mer_list[0]
    first_pair = pair
    prefix = pair[0]
    suffix = pair[1]
    length = len(suffix)
    superstring1 = prefix[length-1:]
    #list to keep track to k-1mer pairs used in cycle 1
    pairs_in_cycle_one = []
    pairs_in_cycle_one.append(pair)

    #cycle one:
    while len(k1mer_list)==len_list:
        count = 0
        for p in k1mer_list:
            #count iterations of loop
            count = count+1
            prefix = p[0]
            #if match found add end to superstring
            if prefix == suffix:
                count=count-1
                if p != first_pair:
                    superstring1 = superstring1 + prefix[length-1:]
                    pairs_in_cycle_one.append(p)
                    suffix = p[1]
                else:
                    #if back to first pair, cycle complete
                    for pa in pairs_in_cycle_one:
                        #remove used k-1mers from list
                        k1mer_list.remove(pa)
                    break
            #if no prefix matches suffix after full for loop break out of loops
            else:
                #based on nymber of iterations of for loop
                if count==len_list:
                    #change condition to break out of while loop
                    len_list = 0
                    break

    len_list=len(k1mer_list)
    pair = k1mer_list[0]
    first_pair = pair
    prefix = pair[0]
    suffix = pair[1]
    superstring2 = prefix[length-1:]
    #list to keep track of k-1mer pairs used in cycle 2
    pairs_in_cycle_two = []
    pairs_in_cycle_two.append(pair)

    #cycle two: same steps as above
    while len(k1mer_list)==len_list:
        count = 0
        for p in k1mer_list:
            count = count+1
            prefix = p[0]
            if prefix == suffix:
                count=count-1
                if p != first_pair:
                    superstring2 = superstring2 + prefix[length-1:]
                    pairs_in_cycle_two.append(p)
                    suffix = p[1]
                else:
                    for pa in pairs_in_cycle_two:
                        k1mer_list.remove(pa)
                    break
            else:
                if count==len_list:
                    len_list = 0
                    break
    
    #if len of k1mer list = 0 after two cycles, then val of k is correct
    if len(k1mer_list)==0:
        print(superstring1)
        #break while loop
        break

            








    
    


