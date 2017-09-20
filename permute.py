import math
import random

def letterswap(string): #randomly swaps two characters in a string
    #
    strlist = list(string)

    if(len(strlist) == 0):
        return
    
    swap1 = random.randint(0, (len(strlist) - 1))
    swap2 = random.randint(0, (len(strlist) - 1))
    strlist[swap1], strlist[swap2] = strlist[swap2], strlist[swap1]
    return strlist

def genUniquePermutations(string): #generates all the unique permutations of a string and returns as list
    strlist = list(string)
    permutations = list()
    guess = strlist
    i = 0
    permutations.append(string)
    while(i < 1000):
        guess = letterswap(guess)
		
        if(guess == None):
            break
        
        if(''.join(guess) in permutations):
            i = i + 1
            continue
        else:
            permutations.append(''.join(guess))
        i = i + 1
    return permutations

def monotonicpaths(pair): #takes tuple, returns list of strings
    pairlist = list()
    pairlist.append(pair)
    monotonicpaths = list()
    for item in (pairstostring(pairlist)):
        monotonicpaths.append(genUniquePermutations(item))
    return monotonicpaths
    
def reachablesquares(maxdist): #takes int, returns int
    i = 0
    squares = 1
    while(maxdist != 0):
        squares = squares + (maxdist * 4)
        maxdist = maxdist - 1
    return squares

def genorderedpairs(maxdist): #takes int, returns list of two-tuples
    x = maxdist
    y = 0
    orderedpairs = list()
    orderedpairs.append((0,0))

    while(len(orderedpairs) != reachablesquares(maxdist)):
        x = random.randint(0, maxdist) # lazy
        tmp = maxdist - x
        
        if(x != maxdist):
            y = random.randint(0, tmp)
        else:
            y = 0

        
            
        if((x,y) in orderedpairs):
            continue
        elif(x == 0 and y == 0):
            continue
        elif(x == 0 and y !=0):
            orderedpairs.append((x, y))
            orderedpairs.append((x, -y))
        elif(x != 0 and y == 0):
            orderedpairs.append((x, y))
            orderedpairs.append((-x, y))
        else:
            orderedpairs.append((x, y))
            orderedpairs.append((-x, y))
            orderedpairs.append((x, -y))
            orderedpairs.append((-x, -y))
        
    return orderedpairs
        
    

def nonmonotonicpaths(endsquare): #takes two-tuple and returns list of strings
    if(abs(endsquare[0]) + abs(endsquare[1]) >= maxdist):
        return
    

def totalpaths():
    pass

def pairstostring(pairs): # takes a list of two-tuples, returns a list of strings
    sequences = list()    
    for item in pairs:
        #print(item)
        temp = list()
        if(item[0] > 0):                        #check x value
            temp.append('r' * abs(item[0]))
        if(item[0] < 0):
            temp.append('l' * abs(item[0]))
        if(item[1] > 0):
            temp.append('u' * abs(item[1]))
        if(item[1] < 0):
            temp.append('d' * abs(item[1]))
        sequences.append(''.join(temp))
    return sequences


def recursivelength(recurlist): # adds list of list
    i = 0
    length = 0
    while(i < len(recurlist)):
        if(type(recurlist[i]) == list):
            length = length + recursivelength(recurlist[i])
        elif(type(recurlist[i]) == str):
            length = length + 1
        i = i + 1
    return length

def removeduplicates(dupelist):
    dupelist = list(set(dupelist))
    
    return dupelist
    
    


      
maxdist = 1
moves = list()

while(maxdist <= 11):
    for item in pairstostring(genorderedpairs(maxdist)):
        for thing in genUniquePermutations(item):
            moves.append(thing)
            moves = list(set(moves))
        #print(item)
        
        #print(moves)
        
    
	print(maxdist, recursivelength(moves))
    maxdist = maxdist + 1
moves = removeduplicates(moves)



            

