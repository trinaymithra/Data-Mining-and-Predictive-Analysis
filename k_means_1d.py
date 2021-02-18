#Clustering of 1d array objects using k means method

arr = [int(i) for i in input("Enter the array: ").split()]
arr = sorted(arr)
n = int(input("Enter number of clusters: "))

mean_arr = list()
for i in range(n) :
    mean_arr.append(int(input("Enter initial mean of "+str(i+1)+"th cluster: ")))

def dist(a,b) :
    return abs(a-b)

def kmeans(n,mean_arr,arr) :
    d = dict()
    for i in range(n) :
        d[i] = []
    
    for i in arr :
    
        dist_arr = list()
    
        for j in mean_arr :
            dist_arr.append(dist(i,j))
        
        #print(dist_arr)
        
        least_dist = min(dist_arr)
        cluster_id = dist_arr.index(least_dist)
        d[cluster_id].append(i)
        
    return d

def mean_calculator(mean_arr,n,d) :
    returned_arr = list()
    for i in range(n) :
        returned_arr.append(sum(d[i])/len(d[i]))
    return returned_arr

while True :
    cur_iter = kmeans(n,mean_arr,arr)
    mean_arr = mean_calculator(mean_arr,n,cur_iter)
    next_iter = kmeans(n,mean_arr,arr)
    if cur_iter == next_iter :
        print("Clusters are: ")
        print(next_iter)
        break
    else :
        mean_arr = mean_calculator(mean_arr,n,next_iter)
