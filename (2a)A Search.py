import queue as Q
from RMP import dict_gn
from RMP import dict_hn

start = 'Arad'
goal = 'Bucharest'
result = ' '

def get_fn(citystr):
    cities = citystr.split(",")
    gn = 0
    for ctr in range(0, len(cities) - 1):
        gn += dict_gn[cities[ctr]][cities[ctr + 1]]
    hn = dict_hn[cities[-1]]
    return hn + gn

def expand(cityq):
    global result
    tot, citystr, thiscity = cityq.get() 
    if thiscity == goal: 
        result = citystr + "::" + str(tot) 
        return 
    for cty in dict_gn[thiscity]: 
        cityq.put((get_fn(citystr + "," + cty), citystr + "," + cty, cty)) 
    expand(cityq)
    
def main(): 
    cityq = Q.PriorityQueue() 
    thiscity = start 
    cityq.put((get_fn(start), start, thiscity)) 
    expand(cityq) 
    print("The A* path with the total is: ") 
    print(result)
main()