x_arr = [float(i) for i in input("Enter all x co-ordinates of the array: ").split()]
y_arr = [float(i) for i in input("Enter all y co-ordinates of the array: ").split()]

points = [tuple((str(x_arr[i])+" "+str((y_arr[i]))).split()) for i in range(len(x_arr))]

n = int(input("Number of clusters: (initial cluster centres would be first 'n' points)"))
centroid_arr = list()

for i in range(n) :
    l = [x_arr[i], y_arr[i]]
    centroid_arr.append(l)
def dist(a,b) :
    return ((float(a[0])-float(b[0]))**2 + (float(a[1])-float(b[1]))**2)**0.5
def kmeans_2d(n,centroid_arr,points) :
    d = dict()
    for i in range(n) :
        d[i] = []    
    for i in points :
        dist_arr = list()
        for j in centroid_arr :
            dist_arr.append(dist(i,j))
        
        least_dist = min(dist_arr)
        cluster_id = dist_arr.index(least_dist)
        d[cluster_id].append(i)        
    return d

def centroid_calculator(n,d) :
    returned_arr = list()
    for i in range(len(d)) :
        x_sum = 0
        y_sum = 0
        for value in d[i] :
            x_sum += float(value[0])
            y_sum += float(value[1])
        if len(d[i]) != 0 :    
            pointer = (x_sum/len(d[i]), y_sum/len(d[i]))
            returned_arr.append(pointer)
        else :
            returned_arr.append((0,0)) 
    return returned_arr

while True :
    cur_iter = kmeans_2d(n,centroid_arr,points)
    centroid_arr = centroid_calculator(n,cur_iter)
    next_iter = kmeans_2d(n,centroid_arr,points)
    if cur_iter == next_iter :
        print("Clusters are: ")
        print(next_iter)
        break
    else :
        centroid_arr = centroid_calculator(n,next_iter)
