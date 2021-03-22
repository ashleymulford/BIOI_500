
file = open("/Users/ashle/Downloads/rosalind_ba10c.txt", "r")

line_list = []

for line in file:
    line_list.append(line.strip("\n"))

#get data from lines in file
path = line_list[0]
alphabet = line_list[2].split("\t")
states = line_list[4].split("\t")
num_alphabet = len(alphabet)
num_states = len(states)
trans_mat = line_list[7:7+num_states]
emiss_mat = line_list[9+num_states:9+num_states*2]
trans_matrix = []
for line in trans_mat:
    trans = line.split("\t")
    trans_matrix.append(trans[1:1+num_states])

emiss_matrix = []
for line in emiss_mat:
    emiss = line.split("\t")
    emiss_matrix.append(emiss[1:1+num_alphabet])


print(path, alphabet, states, trans_matrix, emiss_matrix)

#path = "zxxxxyzzxyxyxyzxzzxzzzyzzxxxzxxyyyzxyxzyxyxyzyyyyzzyyyyzzxzxzyzzzzyxzxxxyxxxxyyzyyzyyyxzzzzyzxyzzyyy"
#alphabet = ["x", "y", "z"]
#states = ["A", "B"]
#trans_matrix = [["0.634", "0.366"], ["0.387", "0.613"]]
#emiss_matrix = [["0.532", "0.226", "0.241"], ["0.457", "0.192", "0.351"]]

num_alphabet = len(alphabet)
num_states = len(states)


viterbi_mat = []

#initialize matrix, initial prob 0.5
initial_prob = 0.5
#iterate through states and alphabet
for i in range(num_states):
    for j in range(num_alphabet):
        if path[0] == alphabet[j]:
            #emission prob * initial prob
            emiss_prob = float(emiss_matrix[i][j])
            prob = initial_prob*emiss_prob
            #append as list
            viterbi_mat.append([prob])

            
#empty matrix to keep track of prev states (same function as arrows)
prev_state_mat = []
for i in range(num_states):
    prev_state_mat.append([])


#fill in both matrices, iterate through path
for i in range(1, len(path)):
    current = path[i]
    #iterate through state and alphabet
    for j in range(num_states):  
        for k in range(num_alphabet):
            #if current letter in path equals alphabet at index k
            if current == alphabet[k]:
                #get emiss prob from matrix at state/alphabet
                emiss_prob = float(emiss_matrix[j][k])
                #get list of transition probs based on state
                trans_prob_list = trans_matrix[j]
                prev_trans_prob_list = []
                #iterate through to get prev prob*transition prob
                #keep track of prev state too
                for l in range(len(trans_prob_list)):
                    #get prev state
                    prev_state = states[l]
                    #get prev and trans probs
                    prev_prob = viterbi_mat[l][i-1]
                    trans_prob = float(trans_prob_list[l])
                    #safe product and prev state to list
                    prev_trans_prob_list.append([prev_prob*trans_prob, prev_state])


                max_state = ""
                max_prob = 0
                #get prev state from which max prob came from
                for item in prev_trans_prob_list:
                    if item[0] > max_prob:
                        max_prob = item[0]
                        max_state = item[1]

                #append max * emiss prob to viterbi matrix
                viterbi_mat[j].append(max_prob*emiss_prob)
                #append prev state to prev state matrix
                prev_state_mat[j].append(max_state)

print(viterbi_mat)
print(prev_state_mat)


#get index of last column in matrix
last = len(viterbi_mat[0])-1

vit_max_state = ""
vit_max_prob = 0

#determine final state for max overall prob
for i in range(num_states):
    if vit_max_prob < viterbi_mat[i][last]:
        vit_max_prob = viterbi_mat[i][last]
        vit_max_state = states[i]

#add final state to string
most_prob_hidden_states = vit_max_state

#traceback, decrement through len of prev state matrix
for i in range(len(prev_state_mat[0])-1, -1, -1):
    #get index for max state
    index = states.index(vit_max_state)
    #add prev state to hidden path string
    most_prob_hidden_states = most_prob_hidden_states + prev_state_mat[index][i]
    #update max state to prev state
    vit_max_state = prev_state_mat[index][i]
    
#traceback got hidden path but backwards, reverse and print
print(most_prob_hidden_states[::-1])












