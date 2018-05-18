import numpy as np
f=open("input.txt",'r')
p=f.read()
t=p.split('\n')#split the input data for \n

maximuminjury=1000000 #given maximum injury
maximumlife=2000 #given maximum life 

n=int(t[0]) #number of monkeys to fight available
t.pop(0) #list of n numbers, each specifying the damage that can be dealt by the monkey
 
for i in range(len(t)): #we convert string into int
    t[i]=int(t[i]) 

maxcountin=0 #maximum count of monkeys that can be defeated as asked in problem
maxcountinlist=[] #we create a list to store maxcount

for i in range(len(t)): #we start here for loop for each element in list
    injury=0 
    count=0
    life=0 #it will count that if life is there or nor or maxinjury has been attained  or just the list has ended
    while (life<maximumlife and injury<maximuminjury and (i+count)<len(t)):
        life=life+t[i+count]
        injury=injury*t[i+count]
        count=count+1
    #here we decrease count by 1 if maxinjuries attained or no life
    if (life>=maximumlife or injury>=maximuminjury):
        count=count-1
    #here we compare maxcountin with new count we get 
    if (count>maxcountin):
        maxcountin=count
        maxcountinlist=[i]
    elif (count==maxcountin): #change maxcountin if new count is greater than we append
        maxcountinlist.append(i)

print(maxcountin) #this prints the maximum number of monkeys that can be defeated
print(len(maxcountinlist)) #this prints the number of times maxcountin value was obtained

