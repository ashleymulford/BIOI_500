
import math

#read in file
file = open("/Users/ashle/Downloads/rosalind_ba8a.txt", "r")

line_list = []

for line in file:
    line_list.append(line)

#get k and m from first line
km = line_list[0].split(" ")
k = int(km[0])
m = int(km[1])

point_list = []
#get points from remaining lines as list of lists
for line in line_list[1:]:
    p = line.split(" ")
    point_list.append(p)


#k = 3
#m = 2
#point_list = [["0.0","0.0"], ["5.0", "5.0"], ["0.0", "5.0"], ["1.0", "1.0"], ["2.0", "2.0"], ["3.0", "3.0"], ["1.0", "2.0"]]


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
        


def farthest_first_traversal(point_list, k, m):
    #choose first point in list to intitalize centers
    centers = [point_list[0]]
    #while length of centers is less than k
    while len(centers) < k:
        #get list of dist for all points 
        dist_all_points = []
        #for all points
        for point in point_list:
            #list of dist for one point, needed in case of multiple centers
            all_dists = []
            #for all centers
            for center in centers:
                #get dist between point and center with m dimensions
                dist = get_distance(point, center, m)
                #add dist to list of all dist for that point
                all_dists.append(dist)
            #euclidean dist used in minimum distance between point and center
            #when multiple centers
            e_dist = min(all_dists)
            #add euclidean dist to list of distance for all point
            dist_all_points.append(e_dist)

        #once euclidean distance determined for all points, find max distance

        max_dist = 0
        index_of_max = 0
        #iterate through list of distances
        for i in range(len(dist_all_points)):
            #save max distance and index
            if max_dist < dist_all_points[i]:
                max_dist = dist_all_points[i]
                index_of_max = i
        #index of max = index of point list where point and center have max distance
        data_point = point_list[index_of_max]
        #add point to list of centers
        centers.append(data_point)

    #return centers when len of list = k
    return centers


centers = farthest_first_traversal(point_list, k, m)

output = open("/Users/ashle/OneDrive/BIOI 500/rosalind/rosalind14_answer.txt", "w")

for c in centers:
    output.write(" ".join(c) + "\n")
        





        
