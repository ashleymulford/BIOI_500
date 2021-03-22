'''
This script determines the last to first mapping position given a burrows-wheeler transform and a postion, returns the corresponding position on the original DNA sequence
'''



#read in file
file = open("/Users/ashle/Downloads/rosalind_ba9k.txt")

lines = []
for line in file:
    lines.append(line.strip("\n"))

bwt = lines[0]
pos = int(lines[1])

print(bwt)
print(pos)

    
#bwt = "T$GACCA"
#pos = 3

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


#get index in first where base equals base at pos in bwt
def last_to_first(bwt, pos):
    #get first string
    first = get_first(bwt)
    #get position dicts for first and bwt
    bwt_pos_dict = get_pos_dict(bwt)
    first_pos_dict = get_pos_dict(first)
    #initialize key and index
    pos_key = ""
    key_index = 0
    #iterate through bwt position dict to find key with value list containing pos
    for key in bwt_pos_dict:
        pos_list = bwt_pos_dict[key]
        for i in range(len(pos_list)):
            #if pos in list save key and index
            if pos_list[i] == pos:
                pos_key = key
                key_index = i
    #get index from first pos dict using key (base) and value list index
    first_index = first_pos_dict[pos_key][key_index]
    return first_index

first_index = last_to_first(bwt, pos)

output = open("/Users/ashle/OneDrive/BIOI 500/rosalind/rosalind12_answer.txt", "w")

output.write(str(first_index))











    





