'''
This script calculates the conditional probability of a string (comprised of the alphabet) given the alphabet, the states, a hidden path (of the states), 
a transition matrix and an emission matrix
'''


file = open("/Users/ashle/Downloads/rosalind_ba10b.txt", "r")

line_list = []

for line in file:
    line_list.append(line.strip("\n"))

path = line_list[0]
alphabet = line_list[2].split("\t")
hidden_path = line_list[4]
states = line_list[6].split("\t")
mat = line_list[9:11]
matrix = []
for line in mat:
    trans = line.split("\t")
    matrix.append(trans[1:4])

#path = "xxyzyxzzxzxyxyyzxxzzxxyyxxyxyzzxxyzyzxzxxyxyyzxxzx"
#alphabet = ["x", "y", "z"]
#hidden_path = "BBBAAABABABBBBBBAAAAAABAAAABABABBBBBABAABABABABBBB"
#states = ["A", "B"]
#matrix = [["0.612", "0.314", "0.074"], ["0.346", "0.317", "0.336"]]


#initial prob
prob = 1

#iterate through path/hidden path (same length)
for i in range(len(path)):
    #get alphabet and state values at current index
    p = path[i]
    h = hidden_path[i]
    #calculate conditional prob and update
    if p == alphabet[0] and h == states[0]:
        prob = prob*float(matrix[0][0])
    elif p == alphabet[0] and h == states[1]:
        prob = prob*float(matrix[1][0])
    elif p == alphabet[1] and h == states[0]:
        prob = prob*float(matrix[0][1])
    elif p == alphabet[1] and h == states[1]:
        prob = prob*float(matrix[1][1])
    elif p == alphabet[2] and h == states[0]:
        prob = prob*float(matrix[0][2])
    else:
        prob = prob*float(matrix[1][2])
    

print(prob)







