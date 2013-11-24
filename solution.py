#/bin/usr/python 

f_odd = []
f_even = []
b_odd = []
b_even =[]

class Player:
    def __init__(self,name,height,score,time):
        self.name = name
        self.height = height
        self.score = score
        self.time = 0 

    def get_name(self):
        return self.name

    def get_score (self):
        return self.score 
    def get_time(self):
        return self.time 
    def more_time(self):
        self.time += 1
    def get_height(self):
        return self.height 
    def time_reset(self):
        self.time = 0 
def better( p1 , p2):
    if ( p1.get_score() > p2.get_score() ):
        return True
    elif ( p1.get_score() <  p2.get_score()):
        return False 
    elif ( p1.get_height() > p1.get_height()):
        return True  
    elif ( p1.get_height() < p1.get_height()):
        return False

def add_draft( player, array):
    if len(array)== 0 :
        array.append(player)
    for i in range(len(array)):
        if i==0:
            if better( array[i],player):
                array.insert(i,player)
                return 
            else:
                continue 
        elif ( 1<= i < len(array) -2):
            cond1 =not(better (array[i],player))#if it's true then player should be next
            cond2  = better( array[i+1],player)
            if (cond1 and cond2):
                array.insert(i,player)
                return 
            else:
                continue
        elif (i == (len(array) -1)) :
            array.append(player)
            return 

def to_bench( on_field):
    ##returns the player that will be sent to the bench 
    out1 = []
    current_longest = 0 
    for player in on_field :
        if player.get_time() >  current_longest:
            del out1[:]
            out1.append(player)
            current_longest = player.get_time()
        elif player.get_time()==  current_longest:
            out1.append(player)
        else:
            continue 
    if len(out1)== 1:
        return out1[0]
    
    out2 =[]
    current_score = 0 
    while player in out2:
        if player.get_score() < current_score:
            del out2[:]
            out2.append(player)
            current_score = player.get_score()
        elif player.get_score() ==  current_score:
            out2.append(player)
        else:
            continue 
        
    if len(out2)==1:
        return out2[0]

    out3 = []
    current_height = 0 
    while player in out3:
        if player.get_height() < current_height:
            del out3[:]
            out3.append(player)
            current_height = player.get_height()
        elif player.get_height() ==  current_height:
            out3.append(player)
        else:
            continue 
    
    if len(out3)==1:
        return out3[0]
        
def to_field( on_bench):
    ##returns the player that will be sent to the bench 
    out1 = []
    current_longest = 100000000000000000000000000000000000000000000000000 
    for player in on_bench :
        if player.get_time() <  current_longest:
            del out1[:]
            out1.append(player)
            current_longest = player.get_time()
        elif player.get_time()==  current_longest:
            out1.append(player)
        else:
            continue 
    if len(out1)== 1:
        return out1[0]
    
    out2 =[]
    current_score = 0 
    for player in out2:
        if player.get_score() > current_score:
            del out2[:]
            out2.append(player)
            current_score = player.get_score()
        elif player.get_score() ==  current_score:
            out2.append(player)
        else:
            continue 
        
    if len(out2)==1:
        return out2[0]

    out3 = []
    current_height = 0 
    for  player in out3:
        if player.get_height() > current_height:
            del out3[:]
            out3.append(player)
            current_height = player.get_height()
        elif player.get_height() ==  current_height:
            out3.append(player)
        else:
            continue 
    
    if len(out3)==1:
        return out3[0]
        
            


def add_time( array):
    #given an array of people on the bench or the field this increments their time 
    for player in array:
        player.more_time()

def is_stats( str):
    #given a str checks if we have the stat file or not
    list = str.split()
#    print "the line is " + line 
#    print "the line is of length:%s "%len(str)
    if len(str) < 3 :
        return False 
    for char in list:
        if char.isdigit() == False:
            return False 
    
    return True 


def make_player(str):
    #given a str makes a player ojbect 
    list = str.split()
    name = list[0]
    height = list[1]
    score = list[2]
    time = 0 
    return Player(name,height,score,0)
    
        
def two_teams( draft):
    #retruns an array of two arrays 
    team_even = draft[0:len(draft)-1:2]
    team_odd = draft[1:len(draft)-1:2]
    return [team_odd,team_even]

def on_feilders( team,p):
    selected = []
    on_field = team[:p]
    on_bench = team[p:]
    return [on_field,on_bench]
    
        
    
def find_remove(p,array):
    index = 0
    print "remove the player by the name: " + p.get_name() + " Score: " + p.get_score()
    for player in array:
#        print "remove the player by the name: " + player.get_name() + " Score: " + player.get_score()
        if( (player.get_score() == p.get_score()) and (player.get_height() == p.get_height())):
            del array[index]
            break 
        else:
            index += 1 
            
        
    
input_file = open("input.txt","r+")
output_file = open("output.txt","w+")


first = 0
draft_array = []
N =0 
M = 0
P =0
case = 0 
for line in input_file.readlines():
    print line
    if ( first == 0 ):
        first = 1
    elif is_stats(line) and (len(line)> 0):
        print "print once"
        list = line.split()
        N = int(list[0])
        M = int(list[1])
        P = int(list[2])
#        print line 
    else:
##        print line
#        print is_stats(line )
        if len(line)>2:
            a_player = make_player(line)
            add_draft(a_player,draft_array)
    ##the 
    if ( len(draft_array) == N ):
#        print "N:" + str(N) +" M:" + str(M)
        #got the teams split 
        draft_No = 0 
        ##-----------------drafted players and their order 
        for player in draft_array:
#            print "Name: " + player.get_name() + " Draft NO: " + str(draft_No) +" Score: " + player.get_score()
            draft_No  += 1 
        ##----------------drafeter players and their order 
        team_even = two_teams(draft_array)[0]
        team_odd = two_teams(draft_array)[1]
        #got the people on the field 
        on_field_even = on_feilders(team_even, P)[0]
        on_field_odd = on_feilders(team_odd, P)[0]
        #got the people on the bench 
        benched_even =  on_feilders(team_even,P)[1]
        
        benched_odd =  on_feilders(team_odd,P)[1]
        for i in range(M):
            #increment the time 
            add_time(on_field_even)
            add_time(on_field_odd)
            
            to_bench_odd = to_bench(on_field_odd)
            to_bench_even = to_bench(on_field_even)
            
            in_for_odd = to_field(benched_odd)
            in_for_even = to_field(benched_even)
            
#            print "%s is in for team odd"%sin_for_odd.get_name()
            print "alsdjflsadkjfasdf " + str(in_for_odd.get_name())
            #remove the players from the bench 
            find_remove(in_for_odd,benched_odd)
            find_remove(in_for_even,benched_even)
            
            #remove players form the field
            find_remove(to_bench_odd,on_field_odd)
            find_remove(to_bench_even,on_field_even)

            #add the going out players to their respective benches 
            benched_odd.append(to_bench_odd)
            benched_even.append(to_bench_even)
            
            #add the going in players to their respctive fields 
            on_field_even.append(in_for_even)
            on_field_odd.append(in_for_odd)
           
        on_field_even.extend(on_field_odd)
        on_field_names = ""
        
        print "done with iterations" 
        for player in on_field_even:
            enter = player.get_name() + " " 
            on_field_names +=  enter 
            print "number of people on the field %s"% len(on_field_names)
            output_file.write("Case #%s: %s\n"%(case,on_field_names))
        case += 1
        

output_file.close()
input_file.close()
            

        
        
        
        
        
