'''
This script reconstructs the original DNA sequence given a burrows-wheeler transform
'''


#read in file
file = open("/Users/ashle/Downloads/rosalind_ba9j.txt")

lines = []
for line in file:
    lines.append(line)

bwt = lines[0].strip("\n")

    
#bwt = "TTCCTAACG$A"

#function to get first column as string from bwt
def get_first(bwt):
    bwt_list = []
    #iterate through string and add char to list
    for l in bwt:
        bwt_list.append(l)
    #sort list lexicographically
    bwt_list.sort()
    #concatenate to get string
    first = ''.join(bwt_list)
    return first

#function to generate dict to keep track of what base is at what position in string
#key are all bases plus $, values are lists of indices
def get_pos_dict(string):
    pos_dict = {}
    #iterate through string
    for i in range(len(string)):
        c = string[i]
        #if char not already a key, add with index as list
        if c not in pos_dict:
            pos_dict[c] = [i]
        #else update existing list with current index
        else:
            pos_dict[c].append(i)
    return(pos_dict)

#function to reconstruct original string from bwt
def reconstruct(bwt):
    #intialize empty seq
    seq = ""
    #get first column from bwt
    first = get_first(bwt)
    #get position dicts for bwt and first
    bwt_pos_dict = get_pos_dict(bwt)
    first_pos_dict = get_pos_dict(first)
    #add first (last) value to string (building in reverse order)
    #iterate through bwt position dict
    for key in bwt_pos_dict:
        pos_list = bwt_pos_dict[key]
        #find key with value list containing position 0 (will be at index 0 in list)
        for i in range(len(pos_list)):
            pos = pos_list[i]
            if pos == 0:
                #add key to seq
                seq = key
    #save current key, now only base in seq
    current_key = seq[0]
    #save current index (must be 0 based on how dict set up, position 0 is at index 0)
    current_index = 0
    #while seq is shorter than bwt, minus 1 to leave off $
    #reconstruct seq in reverse order
    while len(seq) != len(bwt)-1:
        #get next pos from first pos dict using current key/index
        #next pos is the index in the first string of the base that corresponds to the current base in the bwt
        #base in first = base in bwt (i.e. A1 = A1) 
        next_pos = first_pos_dict[current_key][current_index]
        #iterate through bwt position dict to find key (base) with value list that contains next position
        for key in bwt_pos_dict:
            #get list of positions for key
            pos_list = bwt_pos_dict[key]
            #iterate through list
            for i in range(len(pos_list)):
                pos = pos_list[i]
                #if position in list equals next position
                if pos == next_pos:
                    #add key to sequence
                    seq = seq + key
                    #update current key and index
                    current_key = key
                    current_index = i
    #reverse to get reconstructed sequences
    reconstructed_seq = seq[::-1] + "$"
    return reconstructed_seq


r = reconstruct(bwt)

output = open("/Users/ashle/OneDrive/BIOI 500/rosalind/rosalind11_answer.txt", "w")

output.write(r)




