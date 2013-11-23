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
            cond2  = better( array[i+1],player))
            if (con1 and cond2):
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
            del out[:]
            out.append(player)
            current_longest = player.get_time()
        elif player.get_time()==  current_longest:
            out.append(player)
        else:
            continue 
    if len(out1)== 1:
        return out1[0]
    
    out2 =[]
    current_score = 0 
    while player in out:
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
    while player in out2:
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
            del out[:]
            out.append(player)
            current_longest = player.get_time()
        elif player.get_time()==  current_longest:
            out.append(player)
        else:
            continue 
    if len(out1)== 1:
        return out1[0]
    
    out2 =[]
    current_score = 0 
    while player in out:
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
    while player in out2:
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



