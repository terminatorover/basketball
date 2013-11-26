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

                
    print [possible_towns,node_cord,cord_node,dis_start]

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
    #UPDATES DISTANCE

    to_update_neighbours = unvisited_neighbours(town, unvisited)
    no_town = cord_no[town]
    c_d = dis_start[no_town]#the distance from the start to our current town
    
    for n in to_update_neighbours:
        no = cord_no[n]#get the node number for the neighbour 
        dis_neigh = dis_start[no]#get the current shortest distance to the neighbour
        if ( (c_d+1) < dis_neigh ):
            dis_start[no]= c_d + 1
            
def next_node(dis_start,no_cord):
    #returns node number not coordinate 
    first = 1 
    shortest = 0
    for town in dis_start:
        if (first == 1 ) :
            first += 1
            shortest = dis_start[town]
            s_town = town 
        else:
            if ( dis_start[town] < shortest):
                s_town = town 
                shortest = dis_start[town]

    return no_cord[s_town]
                

def find_remove( cord, unvisited):
    where = unvisited.index(cord)
    del unvisited[where]

def is_stats(line):
    ls = line.split()
    if (len(ls)) == 3:
        return True 
    else:
        return False 
        
    
       
        
input_file = open("input.txt","r+")
output_file = open("output.txt","w")


first = 0
no_lines = 0
W = -1
N = -1
H = -1
c_towns = []
for line in input_file.readlines():
    #print line + "length of line is %s"%len(line)
    
    if (first == 0):
        first += 1
    else:
        #this is to check if i have an empty line
        if ( len(line)==1 ):
            continue 
        elif (is_stats(line)):
            ls = line.split()
            W = ls[0]
            H = ls[1]
            N = ls[2]
            c_towns = []
        else:
            print "WTF"
            no_lines += 1
            input = line.split()
            x = int(input[0])
            y = int(input[1])
            c_towns.append((x,y))
            print "c_towns -------------%s"%c_towns
    

    if ( no_lines == N):
         #begin computation 

         print "c_towns -------------%s"%c_towns
         get_data  = data(int(W),int(N),c_towns)
         #setup data 
         unvisited = get_data[0]
         node_cord = get_data[1]
         cord_node = get_data[2]
         dis_start = get_data[3]
         dest = ( int(W),int(N))
         
         current_town = (0,0)
         update_distance( unvisited, current_town, dis_start,node_cord,cord_node)

         find_remove( current_town, unvisited)

         current_town = next_node(dis_start,node_cord)

         while ( current_town != dest):
             update_distance( unvisited, current_town, dis_start,node_cord,cord_node)

             find_remove( current_town, unvisited)

             current_town = next_node(dis_start,node_cord)



         




            
            



