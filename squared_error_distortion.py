'''
This script calculates the squared error distortion given a value k (num of centers), a value m (num of dimensions), a list of centers, and a list of points
'''


import math

#read in file
file = open("/Users/ashle/Downloads/rosalind_ba8b.txt")

line_list = []
#list from lines
for line in file:
    line_list.append(line.strip("\n"))

#get k and m from first line
km = line_list[0].split(" ")
k = int(km[0])
m = int(km[1])

#get centers from next lines based on k
centers = line_list[1:1+k]
centers_list = []
#get list of lists
for item in centers:
    centers_list.append(item.split(" "))

#gte points from remaining lines
points = line_list[2+k:]
points_list = []
#get list of lists
for item in points:
    points_list.append(item.split(" "))

#k = 2
#m = 2
#centers_list = [["2.31", "4.55"], ["5.96", "9.08"]]
#points_list = [["3.42", "6.03"], ["6.23", "8.25"], ["4.76", "1.64"], ["4.47", "4.33"], ["3.95", "7.61"], ["8.93", "2.97"], ["9.74", "4.03"], ["1.73", "1.28"], ["9.72", "5.01"], ["7.27", "3.77"]]

#get Euclidean distance between point1 and point2 with m number of dimensions
def get_distance(point1, point2, m):
    sum_of_squares = 0
    #for each dimension get the difference and square, then sum up
    for i in range(m):
        diff = float(point1[i])-float(point2[i])
        sum_of_squares += diff**2
    #square root the sum of all squares to get the distance
    dist = math.sqrt(sum_of_squares)
    return dist 

def get_distortion(centers_list, points_list, k, m):
    #get number of points in list
    n = len(points_list)
    sum_of_squared_dists = 0
    #for all points
    for point in points_list:
        #list of dist for one point, needed in case of multiple centers
        all_dists = []
        #for all centers
        for center in centers_list:
            #get dist between point and center with m dimensions
            dist = get_distance(point, center, m)
            #add dist to list of all dist for that point
            all_dists.append(dist)
        #euclidean distance is minimum distance
        e_dist = min(all_dists)
        #add squared euclidean distance to sum
        sum_of_squared_dists += e_dist**2
    #calculate distortion: sum/number of points, round to 3 decimal places 
    distortion = round(sum_of_squared_dists/n, 3)
    return distortion

print(get_distortion(centers_list, points_list, k, m))





    
    
