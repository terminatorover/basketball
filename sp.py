#usr/bin/python 

from tabulate import tabulate
    

unvisited = []

def f(list):
    new_list = []
    for tuple in list:
        x = tuple[0]
        y = tuple[1]
        new_list.append((x-1,y))
    return new_list 

def data( W, N,c_towns):
    #you need to create and pass in c_towns from the input file 
    
    #node number  to (x,y) coordinate 
    #(x,y) coordinate to node number
    
    #distance from start, node /distance, #initializing 
    dis_start = {}
   # print tabulate(table)
    

    no = 1
    node_cord = {}
    cord_node = {}
    node_start = {}
    possible_towns  = [] 
    matrix = []
    for row in range(N+1):
        array = []
        for col in range(W+1) :

            if (col,row) in (c_towns):

                array.append("C_T(%s,%s)"%(col,row))
  #             
                continue 
            else:
                possible_towns.append((col,row))
                #updates the dictionary 
                node_cord[no]=(row,col)
                cord_node[(col,row)]=no 
                if (  (row,col)== (0,0)):
#                    print "x "
                    array.append("(%s,%s)"%(col,row))

                    dis_start[no] = 0
                    node_start[no] = []
                else:
 #                   print "- "
                    array.append("(%s,%s)"%(col,row))

#                    print str((x,y)) + " - " 
                    
              #      table[y][x]="88"
                  #  print tabulate(table)
                    dis_start[no] = 1000000000000000000000000000000000000000000000000000000000
                    node_start[no] = []
                no += 1
        matrix.append(array)
        
                

    print tabulate(matrix)
                
    return  [possible_towns,node_cord,cord_node,dis_start,node_start]

data(10,3,[(3,1),(10,3)])
def unvisited_neighbours(town, unvisited):
    x = town[0]
    y = town[1]
    u_n = [] #unvisited neighbours
    for i in range(-1,2):
        for j in range(-1,2):
            if ((x+i,j+1)) in unvisited:
                u_n.append((x+i,j+1))
                
    return u_n #a list of (x,y) coordinates
            

def update_distance( univisited, town, dis_start,node_start,no_cord,cord_no):
    #UPDATES DISTANCE

    to_update_neighbours = unvisited_neighbours(town, unvisited)
    no_town = cord_no[town]
    c_d = dis_start[no_town]#the distance from the start to our current town
    c_ns = node_start[no_town]#the nodes to the current town
    
    for n in to_update_neighbours:
        no = cord_no[n]#get the node number for the neighbour 
        dis_neigh = dis_start[no]#get the current shortest distance to the neighbour

        if ( (c_d+1) < dis_neigh ):
            dis_start[no]= c_d + 1
            node_start[no] = c_ns.append(no)
            
            
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
    
    try:
        where = unvisited.index(cord)
#        print "UNVISITED %s COORDINATES:%s Where:%s"%(unvisited,cord,where)
        del unvisited[where]
#        break 
        return 
        
    except ValueError:
        print "Cord doesn't exist"

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
'''
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
            c_towns.append((x-1,y-1))
#            print "c_towns -------------%s"%c_towns
    
#    print "no_lines---:%s N-----:%s"%(no_lines,N)
    if ( int(no_lines) == int(N)):
         #begin computation 
         print "////////////////\\\\\\\\\\\\\\\\"
         print "*****************%s***********"%line
         #print "c_towns -------------%s"%c_towns
         #
#         print "W:%s H:%s N:%s"%(W,H,N) 
         get_data  = data(int(W),int(N),c_towns)
         #setup data 
         unvisited = get_data[0]
         node_cord = get_data[1]
         cord_node = get_data[2]
         dis_start = get_data[3]
         nodes_start = get_data[4]
         dest = ( int(W),int(N))
         
         current_town = (0,0)
         update_distance( unvisited, current_town, dis_start,nodes_start,node_cord,cord_node)
         
         find_remove( current_town, unvisited)

         current_town = next_node(dis_start,node_cord)
#         print "c_towns **************************-------------%s"%current_town
         

         while ( current_town != dest):
             print "WTF------------------------"
             update_distance( unvisited, current_town, dis_start,nodes_start,node_cord,cord_node)

             find_remove( current_town, unvisited)

             current_town = next_node(dis_start,node_cord)
         
      #   print nodes_start[current_town]


         




            '''
            



