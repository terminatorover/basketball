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

def add_draft_2( player, array):
#    print player.get_name()
    if len(array)== 0 :
        array.append(player)
    for i in range(len(array)):
        if i==0:
            if better( array[i],player):
#                array.insert(i,player)
                array.append(player)
     #           return 
            else:
                continue 
        elif ( 1<= i < len(array) -2):
            cond1 =(better (array[i],player))#if it's true then player should be next
            cond2  = not (better( array[i+1],player)) 
            if (cond1 and cond2):
                array.insert(i+1,player)
    #            return 
            else:
                continue
        elif (i == (len(array) -1)) :
            array.append(player)
   #         return 
    names = []
    for player in array:
        names.append(player.get_name())


def order_h( player_arr):
    height_player_dic = {}
    height_index = []
    for player in player_arr:
        tall = player.get_height()
        height_index.append(tall)
        height_player_dic[tall] = player
    
    height_index.sort()
    new_arr  = []
    for height in height_index:
        new_arr.append(height_player_dic[height])
    player_arr = new_arr

def add_draft(player1, score_player_set):

    if len(score_player_set)==0:
        score = int(player1.get_score())
        score_player_set[score]=[ player1]
    else :
        score = int(player1.get_score())
        if score in score_player_set:
            score_player_set[score].append(player1)
            order_h(score_player_set[score])
        else:
            score_player_set[score]=[ player1]
    
def no_players( dic):
    count = 0 
    score_list = dic.keys()
    score_list.sort()
    for score in score_list:
        count += len(dic[score])
    return count 

def arraify( dic ):
    array = []
    score_list = dic.keys()
    score_list.sort()
    me = Player("Robera","11","100",0)
    for score in score_list:
#        array.extend(dic[score])
        for player in dic[score]:
            if type(me)==type(player):
                array.append(player)
            
    return array 

        
    

        




def to_bench_2( on_field):
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
        
def to_bench(on_field, p_d):
    #take in an array of players on the field and returns the player to go out
    time_players = {}

    for player in on_field:
        time = player.get_time()
        if time in time_players:
            time_players[time].append(player)
        else:
            time_players[time]=[player]
    
    times = time_players.keys()
#    print times
    times.sort()
    le = len(times)

    longest_time = times[-1]
    possible_people = time_players[longest_time]
    if len(possible_people) == 1:
        return possible_people[0]
    else:
        worst_player =  possible_people[0]
        for player in possible_people:
            if ( p_d[player] > p_d[worst_player]):
                worst_player = player

    return worst_player
            
            

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
#        print "add time for %s"%player.get_name()
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
    team_even = draft[0::2]
    team_odd = draft[1::2]
    return [team_odd,team_even]

def on_feilders( team,p):
    selected = []
    on_field = team[:p]
    on_bench = team[p:]
    return [on_field,on_bench]
    
        
    
def find_remove(p,array):
    index = 0
#    print p
#    print "remove the player by the name: " + p.get_name() + " Score: " + p.get_score()
    for player in array:
#        print "remove the player by the name: " + player.get_name() + " Score: " + player.get_score()
        if( (player.get_score() == p.get_score()) and (player.get_height() == p.get_height())):
            del array[index]
            break 
        else:
            index += 1 
            
def remove_non_player(array):
    me = Player("Robera","11","100",0)
    index = 0 
    for player in array:
        if type(player) != type(me):
            del array[index] 
        else:
            index += 1
        
            

    
input_file = open("input.txt","r+")
output_file = open("output.txt","w+")


first = 0
draft_array = []
draft_dic = {}
N = 10000000000000000000000000000000000000000000000000
M = 10000000000000000000000000000000000000000000000000
P = 10000000000000000000000000000000000000000000000000
case = 1
for line in input_file.readlines():
    print line
    if ( first == 0 ):
        first = 1
    elif is_stats(line) and (len(line)> 2):
        print "print once"
        list = line.split()
        print list 
        N = int(list[0])
        M = int(list[1])
        P = int(list[2])
#        draft_array = []
#        print line 
    else:
##        print line
#        print is_stats(line )
        if len(line)>2:
#            print " player to be added and stats: " + line 
            a_player = make_player(line)
            add_draft(a_player,draft_dic)

            #print "N:" + str(N) +" M:" + str(M) + "len of draft array: %s"%len(draft_array)
    #-------------------computation ---------------------------------------
    if ( no_players(draft_dic) == N and len(line)>2):

        print "------------------------ONCE3----------------------------------" 
        draft_array = arraify(draft_dic)
        draft_array.reverse()
        remove_non_player(draft_array)

        #have a player to draft number dic 
        draft_index = 0 
        player_to_no = {}#PLAYER TO DRAFT NO INDEX
        for player in draft_array:
            
            player_to_no[player]= draft_index
            draft_index += 1 

##  printing the players and their draft numbers      
        for player in player_to_no:
           print "Player name: %s Draft_no: %s"%(player.get_name(),player_to_no[player])


        
        #got the teams split 
        draft_No = 0 
        ##-----------------drafted players and their order 
        for player in draft_array:
            print "Name: " + player.get_name() + " Draft NO: " + str(draft_No) +" Score: " + player.get_score()
            draft_No  += 1 
        ##----------------drafeter players and their order 
        team_even = two_teams(draft_array)[0]
        team_odd = two_teams(draft_array)[1]
#        '''
        

        #trying to check if the teams are right 
        team_odd_str = ""
        team_even_str = ""
        for o_p in team_odd:
 #           print "player on team odd--------------> %s"%o_p.get_name()
            team_odd_str += (" %s "%o_p.get_name() )
        for e_p in team_even:
#            print "player on team even --------------> %s"%e_p.get_name()
            team_even_str += (" %s "%e_p.get_name())

        print "Team even:--------------------------> %s\n"% team_odd_str
        print "Team odd:----------------------------> %s\n"% team_even_str
 #       '''
        #got the people on the field 
        on_field_even = on_feilders(team_even, P)[0]
        on_field_odd = on_feilders(team_odd, P)[0]
        
        #got the people on the bench 
        benched_even =  on_feilders(team_even,P)[1]
        
        benched_odd =  on_feilders(team_odd,P)[1]
        
        ##odd players and even players on the field at the start
        '''
        on_e = ""
        on_o = ""
        
        for e_p in on_field_even:
#            print "even player on the the field %s"% e_p.get_name()
            on_e += " %s "%e_p.get_name()

        for o_p in on_field_odd:
            on_o += " %s "%o_p.get_name()
        
        print "On field for odd -**********************%s"%on_o
        print "On field for  even-**********************%s"%on_e
'''
        for i in range(M):
            #increment the time 
            on_e = ""
            on_o = ""
            for e_p in on_field_even:
            #            print "even player on the the field %s"% e_p.get_name()
                on_e += " %s "%e_p.get_name()

            for o_p in on_field_odd:
                on_o += " %s "%o_p.get_name()
        
            print "On field for odd -**********************%s"%on_o
            print "On field for  even-**********************%s"%on_e

#            for player in on_field_even :
#                print "Player Name : %s"% player.get_name() 
            
            add_time(on_field_even)
            add_time(on_field_odd)
            
            to_bench_odd = to_bench(on_field_odd,player_to_no)
            to_bench_even = to_bench(on_field_even,player_to_no)
            
            in_for_odd = to_field(benched_odd)
            in_for_even = to_field(benched_even)
            
#            print "%s is in for team odd"%sin_for_odd.get_name()
#            print "player to go in for ODD: " + str(in_for_odd.get_name())
            #remove the players from the bench 
            find_remove(in_for_odd,benched_odd)
            find_remove(in_for_even,benched_even)
#            print "player to go out for ordd: " + str(to_bench_odd.get_name())
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
        on_field_names = []
        
        print "done with iterations" 
        for player in on_field_even:
            print "WTF"
            on_field_names.append(player.get_name())
        
        
        on_field_names.sort()#lexographic ordering 
        names_to_return = ""
        for name in on_field_names:
            names_to_return += "%s "%name
            

        output_file.write("Case #%s: %s\n"%(case,names_to_return ))
        case += 1
output_file.close()
input_file.close()
            

        
        
        
        
        
