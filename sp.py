#usr/bin/python 


    

unvisited = []


def data( W, N,c_towns):
    #you need to create and pass in c_towns from the input file 
    
    #node number  to (x,y) coordinate 
    #(x,y) coordinate to node number
    
    #distance from start, node /distance, #initializing 
    dis_start = {}
    
    no = 1
    node_cord = {}
    cord_node = {}
    
    possible_towns  = [] 
    for x in range(W+1):
        for y in range(N+1) :
            if (x,y) in c_towns:
                continue 
            else:
                possible_towns.append((x,y))
                #updates the dictionary 
                node_cord[no]=(x,y)
                cord_node[(x,y)]=no 
                if (  (x,y)== (0,0)):
                    dis_start[no] = 0
                else:
                    dis_start[no] = 1000000000000000000000000000000000000000000000000000000000
                no += 1

                
    print possible_towns 

def unvisited_neighbours(town, unvisited):
    x = town[0]
    y = town[1]
    u_n = [] #unvisited neighbours
    for i in range(-1,2):
        for j in range(-1,2):
            if ((x+i,j+1)) in unvisited:
                u_n.append((x+i,j+1))
                
    return u_n #a list of (x,y) coordinates
            

def update_distance( univisited, town, dis_start,no_cord,cord_no):
    to_update_neighbours = unvisited_neighbours(town, unvisited)
    no_town = cord_no[town]
    c_d = dis_start[no_town]#the distance from the start to our current town
    
    
    for n in to_update_neighbours:
        no = cord_no[n]#get the node number for the neighbour 
        dis_neigh = dis_start[no]#get the current shortest distance to the neighbour
        if ( (c_d+1) < dis_neigh ):
            dis_start[no]= c_d + 1
            
       
        
    return 0 
    
    

data(1,1,[(1,0),(1,1)])
