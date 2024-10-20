import queue as Q
from RMP import dict_gn
from RMP import dict_hn

start = 'Arad'
goal = 'Bucharest'
result = ''

def get_fn(citystr):
    cities = citystr.split(",")
    gn = 0
   
    for ctr in range(0, len(cities) - 1):
        gn += dict_gn[cities[ctr]][cities[ctr + 1]]
   
    hn = dict_hn[cities[-1]]
    return gn + hn

def printout(cityq):
    
    for i in range(0, cityq.qsize()):
        print(cityq.queue[i])

def expand(cityq):
    global result
    
    if cityq.empty():
        return
    
    tot, citystr, thiscity = cityq.get()
    nexttot = float('inf')
    
    if not cityq.empty():
        nexttot, nextcitystr, nextthiscity = cityq.queue[0]

    if thiscity == goal:
        result = citystr + ":" + str(tot)
        return

    print("Expanded city -------", thiscity)
    print("Second best f(n)------", nexttot)

    tempq = Q.PriorityQueue()
    
    for cty in dict_gn[thiscity]: 
        tempq.put((get_fn(citystr + ',' + cty), citystr + ',' + cty, cty)) 

    for ctr in range(1, 3): 
        if tempq.empty():
            break
        
        ctrtot, ctrcitystr, ctrthiscity = tempq.get()
        
        if ctrtot < nexttot:
            cityq.put((ctrtot, ctrcitystr, ctrthiscity)) 
        else:  
            cityq.put((ctrtot, citystr, thiscity)) 
            break 
    
    printout(cityq) 
    expand(cityq)

def main(): 
    cityq = Q.PriorityQueue() 
    thiscity = start 
    cityq.put((float('inf'), "NA", "NA"))
    cityq.put((get_fn(start), start, thiscity)) 
    expand(cityq) 
    print(result) 

main()