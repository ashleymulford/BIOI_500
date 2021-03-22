'''
This script calculates the probability of a hidden path given the hidden path, states, and transition matirx
'''


file = open("/Users/ashle/Downloads/rosalind_ba10a.txt", "r")

line_list = []

for line in file:
    line_list.append(line.strip("\n"))

path = line_list[0]
states = line_list[2].split("\t")
mat = line_list[5:7]
matrix = []
for line in mat:
    trans = line.split("\t")
    matrix.append(trans[1:3])


#path = "AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB"
#states = ["A", "B"]
#matrix = [["0.194", "0.806"], ["0.273", "0.727"]]


#initial prob is equal for both states
prob = 0.5

#iterate through path
for i in range(len(path)-1):
    #get current and next states
    start = path[i]
    end = path[i+1]
    #calculate transition prob and update
    if start == states[0] and end == states[0]:
        prob = prob*float(matrix[0][0])
    elif start == states[0] and end == states[1]:
        prob = prob*float(matrix[0][1])
    elif start == states[1] and end == states[0]:
        prob = prob*float(matrix[1][0])
    else:
        prob = prob*float(matrix[1][1])

print(prob)
