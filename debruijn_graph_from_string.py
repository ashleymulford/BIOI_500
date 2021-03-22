'''
This script creates a debruijn graph given a string and a value of k, output as an adjacency list
'''


file = open("/Users/ashle/Downloads/rosalind_ba3d.txt")

info = []

#add info from file to list
for line in file:
    info.append(line.strip("\n"))

#save values 
k = int(info[0])
seq = info[1]


#k = 4
#seq = "AAGATTCTCTAC"


#function to get all kmers from a sequence, outputs a list
def get_kmers(seq, k):
    kmers = []
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        kmers.append(kmer)
    return kmers


kmers_list = get_kmers(seq, k)

adj_list = []

#iterate through list of kmers
for kmer in kmers_list:
    #create a pair of k-1mers
    k_1mers = []
    k_1mers.append(kmer[0:k-1])
    k_1mers.append(kmer[1:k])

    #track if added to adjacency list
    added = False

    #if adjacency list not empty
    if len(adj_list) != 0:
        #iterate through items in adjacency list
        for item in adj_list:
            #if two prefixes match append item with new suffix
            if item[0] == k_1mers[0]:
                item.append(k_1mers[1])
                #track added
                added = True
                #break once added if match found
                break
            
    #check if already added so as to not add twice
    if added == False:
        #add if not already added via appending existing item
        adj_list.append(k_1mers)


output = open("/Users/ashle/OneDrive/BIOI 500/rosalind/rosalind7_answer.txt", "w")

#output list to file in proper format
for item in adj_list:
    if len(item) == 2:
        output.write(item[0]+ " -> " + item[1] + "\n")
    else:
        prefix = item[0]
        suffixs = item[1:]
        output.write(prefix + " -> ")
        for i in range(len(suffixs)):
            suf = suffixs[i]
            if i != (len(suffixs)-1):
                output.write(suf + ",")
            else:
                output.write(suf + "\n")











    
