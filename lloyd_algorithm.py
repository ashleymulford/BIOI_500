
import math


#read in file
file = open("/Users/ashle/Downloads/rosalind_ba8c.txt", "r")

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


#k = 2
#m = 2
#points_list = [["1.3", "1.1"], ["1.3", "0.2"], ["0.6", "2.8"], ["3.0", "3.2"], ["1.2", "0.7"], ["1.4", "1.6"], ["1.2", "1.0"], ["1.2", "1.1"], ["0.6", "1.5"], ["1.8", "2.6"], ["1.2", "1.3"], ["1.2", "1.0"], ["0.0", "1.9"]]


#get Euclidean distance between point1 and point2 with m dimensions
def get_distance(point1, point2, m):
    sum_of_squares = 0
    #for each dimension get the difference and square, then sum up
    for i in range(m):
        diff = float(point1[i])-float(point2[i])
        sum_of_squares += diff**2
    #square root the sum of all squares to get the distance
    dist = math.sqrt(sum_of_squares)
    return dist

#get center of gravity from points in cluster with m dimensions
def get_cent_of_gravity(cluster_list, m):
    #initialize list for point that will be center of gravity
    cent_of_gravity = []
    n = len(cluster_list)
    #iterate through dimensions
    for i in range(m):
        sum_at_dim = 0
        #iterate through points
        for point in cluster_list:
            #get sum at each dimension
            sum_at_dim += float(point[i])
        #calculate average
        average_at_dim = round(sum_at_dim/n, 3)
        #add average to list, center of gravity is average value at each dimension
        cent_of_gravity.append(str(average_at_dim))
    return cent_of_gravity
        

def get_best_centers(points_list, k, m):
    #initial centers from first k points
    centers = points_list[0:k]
    optimal = False
    #while centers not optimal
    while not optimal:
        #initialize dict for clusters, key is clust number (corresponds to num of centers)
        #value is list of points in cluster
        clusters = {}
        #iterate through points
        for point in points_list:
            all_dists = []
            #iterate through centers
            for center in centers:
                #get dist between each point and center and save in list
                dist = get_distance(point, center, m)
                all_dists.append(dist)
            #determine cluster to add point to based on min distance
            clust_num = 0
            #get min distance
            min_dist = min(all_dists)
            #go through list of all distances
            for i in range(len(all_dists)):
                dist = all_dists[i]
                #if dist at i equals min dist
                if dist == min_dist:
                    #i is clust num, break loop
                    clust_num = i
                    break
            #add point to clust num value list in dict
            #if clust num already a key, append list
            if clust_num in clusters.keys():
                clusters[clust_num].append(point)
            #if new key, add with point in list
            else:
                clusters[clust_num] = [point]
        new_centers = []
        #once each point assigned to cluster
        #get center of gravity for each cluster and add to new centers list
        for clust_num in clusters:
            new_centers.append(get_cent_of_gravity(clusters[clust_num], m))
        #if new centers equals current centers then optimal centers are found
        if new_centers == centers:
            #end loop and return optimal centers
            optimal = True
            return new_centers
        #if different, repeat process
        else:
            centers = new_centers

centers = get_best_centers(point_list, k, m)

for c in centers:
    print(" ".join(c))








