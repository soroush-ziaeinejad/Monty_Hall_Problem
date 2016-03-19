from random import *

win=0
lose=0
for i in range(1000000):
    rewards=["Goat","Goat","Car"]
    doors=[]
    k=3
    for j in range(3):
        if(k>0):
            r=randrange(k)
            a=rewards[r]
            doors.append(('Door '+str(j), a))
            k=k-1
            rewards.remove(rewards[r])
    c = randrange(3)
    d = randrange(3)
    while d==c or doors[d][1]!='Goat':
        d = randrange(3)
    if doors[3-c-d][1]=="Car":
        win+=1
    else:
        lose+=1
print ("WIN: ",win)
print ("LOSE: ",lose)
