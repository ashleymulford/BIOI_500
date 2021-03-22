'''
This scripts determines clusters using hierarchical clustering given a value n and and nxn distance matirx, 
outputs each cluster one by one until all points are within one cluster
'''


import math

file = open("/Users/ashle/Downloads/rosalind_ba8e (1).txt")

line_list = []

for line in file:
    line_list.append(line.strip("\n"))

n = int(line_list[0])
rest = line_list[1:]

matrix = []

for line in rest:    
    row = line.split(" ")
    matrix.append(row)

'''
n = 7
matrix = [["0.00", "0.74", "0.85", "0.54", "0.83", "0.92", "0.89"],
["0.74", "0.00", "1.59", "1.35", "1.20", "1.48", "1.55"],
["0.85", "1.59", "0.00", "0.63", "1.13", "0.69", "0.73"],
["0.54", "1.35", "0.63", "0.00", "0.66", "0.43", "0.88"],
["0.83", "1.20", "1.13", "0.66", "0.00", "0.72", "0.55"],
["0.92", "1.48", "0.69", "0.43", "0.72", "0.00", "0.80"],
["0.89", "1.55", "0.73", "0.88", "0.55", "0.80", "0.00"]]
'''

#function to get smallest distance from matrix
def get_smallest_distance(matrix, n):
    #save all dist to list
    dist_list = []
    #save all distance and indices to list of lists
    dist_index_list = []
    #iterate through row, i=row number
    for i in range(n):
        #iterate through columns, j=column number
        #range starts at i+1 to avoid 0s and duplicates
        for j in range(i+1, n):
            dist = matrix[i][j]
            dist_list.append(dist)
            dist_index_list.append([dist, i, j])
    #get min distance from list of only distances
    min_dist = min(dist_list)
    #initialize row/column numbers
    row_number = 0
    column_number = 0
    #iterate through to find row/column numbers for min distance
    for item in dist_index_list:
        if item[0] == min_dist:
            row_number = item[1]
            column_number = item[2]
            break
    #return row and column numbers
    return row_number, column_number
            

#function to get cluster (determine groups from row/column numbers using dict)
def get_cluster(row_to_group_dict, row_number, column_number):
    #cluster is a list of the groups in the cluster
    cluster = []
    #cluster must be formed as new/shorter group added to cluster first unless same length
    #if same length, smaller number first
    if len(row_to_group_dict[row_number]) == len(row_to_group_dict[column_number]):   
        #get group numbers from dict at both row and column numbers
        #row first, as smaller number
        for item in row_to_group_dict[row_number]:
            cluster.append(str(item))
        for item in row_to_group_dict[column_number]:
            cluster.append(str(item))
    elif len(row_to_group_dict[row_number]) < len(row_to_group_dict[column_number]):
        #get group numbers from dict at both row and column numbers
        #row first, as shorter group length
        for item in row_to_group_dict[row_number]:
            cluster.append(str(item))
        for item in row_to_group_dict[column_number]:
            cluster.append(str(item))
    elif len(row_to_group_dict[row_number]) > len(row_to_group_dict[column_number]):
        #get group numbers from dict at both row and column numbers
        #column first, as shorter group length
        for item in row_to_group_dict[column_number]:
            cluster.append(str(item))
        for item in row_to_group_dict[row_number]:
            cluster.append(str(item))
        
    return cluster

#update dictionary so row/column for cluster is now represented as one
def update_dict(row_to_group_dict, row_number, column_number, current_cluster):
    #row number will always be smaller than column number
    #assign current cluster as value to smaller key (row_number) in dict
    row_to_group_dict[row_number] = current_cluster
    #remove column number as value is now represented in row number
    #as part of current cluster
    row_to_group_dict.pop(column_number)
    #if column number isnt last last/row in matrix
    if column_number != len(row_to_group_dict):
        #iterate trhough and shift all values past column number by one
        for i in range(column_number+1, len(row_to_group_dict)+1):
            #original key is i, new key is one less than i to shift by one
            key = i-1
            #get value from original key
            value = row_to_group_dict[i]
            #add new key and original value to dict
            row_to_group_dict[key] = value
            #pop original key
            row_to_group_dict.pop(i)
    return row_to_group_dict

#function to update matrix once cluster is formed
#take the average distance and combine row/column to get new matrix of (n-1 x n-1)
def update_matrix(matrix, row_to_group_dict, row_number, column_number):
    #m is n-1 as dict updated first in main function
    m = len(row_to_group_dict)
    #empty matrix
    new_matrix = []
    #get list of average dists between row number dist and col number dist
    average_dist = []
    #iterate through rows in current matrix
    for i in range(m+1):
        #skip column number so 0.00 does not appear twice
        if i != column_number:
            #take avergae of both distances
            d1 = matrix[i][row_number]
            d2 = matrix[i][column_number]
            average = (float(d1)+float(d2))/2
            #append as string for type consistency
            average_dist.append(str(average))

    #use original matrix and average dist list to build new matrix
    #iterate through row, i=row number when iterating in matrix
    for i in range(m+1):
        #build new matrix row by row
        new_row = []
        #iterate through columns, j=column number when iterating in matrix
        for j in range(m+1):
            #if neither row or column = row or column number then use orginal dists
            if i != row_number and i != column_number and j != row_number and j != column_number:
                new_row.append(matrix[i][j])
            #skip when i (row) is column number so as to not duplicate
            elif i == column_number:
                continue
            #when row is row number new row is average dist list
            #this row in new matrix represents current cluster 
            elif i == row_number:
                new_row = average_dist
            #skip when j (coulmn) is column number so as to not duplicate
            elif j == column_number:
                continue
            #this fills in position in new row that represent the column in new matrix
            #that represents current cluster
            elif j == row_number:
                #average dist list is one short than matrix
                #if i (row) is less than or equal to len of average dist list
                if i <= len(average_dist):
                    #up to and including column number, dist is average dist at i
                    if i <= column_number:
                        new_row.append(average_dist[i])
                    #after row passes column number, dist is average dist at i-1
                    if i > column_number:
                        new_row.append(average_dist[i-1])
        #add new row to new matrix as along as row is not empty      
        if len(new_row) > 0:
            new_matrix.append(new_row)            
    return new_matrix
    
        
def hierarchical_clustering(matrix, n):
    #set up initial row to group dict
    #keep track of which row/column numbers correspond to which group numbers
    row_to_group_dict = {}
    for i in range(n):
        row_to_group_dict[i] = [i+1]

    #store all_clusters for output
    all_clusters = []
    
    #empty cluster list
    cluster = []

    #whule cluster does not contain all groups
    while len(cluster) < n:
        #get row/column combo that produces smallest dist
        row_number, column_number = get_smallest_distance(matrix, len(row_to_group_dict))
        #determine which group or cluster of groups are represented by row/column
        #and form new combined cluster 
        current_cluster = get_cluster(row_to_group_dict, row_number, column_number)
        #add cluster to list
        all_clusters.append(current_cluster)
        #update row_to_group_dict, one less key
        row_to_group_dict = update_dict(row_to_group_dict, row_number, column_number, current_cluster)
        #update matrix, one less row/column
        matrix = update_matrix(matrix, row_to_group_dict, row_number, column_number)
        #update cluster to curretn cluster
        cluster = current_cluster
    return all_clusters


all_clusters = hierarchical_clustering(matrix, n) 


#output each cluster:
for item in all_clusters:
    print(" ".join(item))












    
