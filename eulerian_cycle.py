import random

file = open("/Users/ashle/Downloads/rosalind_ba3f.txt", "r")

#initialize dictionary
adj_dict = {}

#fill dictionary: key is start node, value is list of adjacent nodes
for line in file:
    line_ = line.strip("\n")
    line_list = line_.split(" -> ")
    start = line_list[0]
    rest = line_list[1]
    ends = []
    #if multiple adjacent nodes split by , to create list
    if len(rest) > 1:
        ends = rest.split(",")
        adj_dict.update({start:ends})
    #if one adjacent node add to list
    else:
        ends.append(rest)
        adj_dict.update({start:ends})


#adj_dict = {'0':['3'], '1':['0'], '2':['1','6'], '3':['2'], '4':['2'], '5':['4'], '6':['5','8'], '7':['9'], '8':['7'], '9':['6']}


#determine number of edges:
num_edges = 0
for key,value in adj_dict.items():
    num_edges += len(value)


#initialize empty cycle
cycle = []

#choose random start
start = random.choice(list(adj_dict.items()))

#get current node from start
current_node = start[0]

#while cycle does not contain all edges
while len(cycle) != num_edges:
    #get list of connected nodes
    edge_nodes = adj_dict[current_node]
    #if list not empty
    if len(edge_nodes) != 0:
        #add current node to cycle
        cycle.append(current_node)
        #get new current node from firt adjacent node in list
        current_node = edge_nodes[0]
        #remove new current node from list
        edge_nodes.pop(0)
        #print(cycle)
    #if list is empty
    else:
        #print(adj_dict)
        #go through nodes in existing cycle and find one with a non-empty list
        for i in range(len(cycle)):
            key = cycle[i]
            if len(adj_dict[key]) != 0:
                #update current node to one with non-empty list
                current_node = key
                #fix order of cycle to start with new current node
                front_cycle = cycle[i:]
                back_cycle = cycle[0:i]
                cycle = front_cycle + back_cycle
                #print(cycle)
                #end loop once one is found
                break

#add in last current node to complete cycle
cycle.append(current_node)

#output to file
output = open("/Users/ashle/OneDrive/BIOI 500/rosalind/rosalind9_answer.txt", "w")

#add -> after all nodes except last one
for i in range(len(cycle)):
    if i != len(cycle)-1:
        node = cycle[i]
        output.write(node + "->")
    else:
        node = cycle[i]
        output.write(node)
        





