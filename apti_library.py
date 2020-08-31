import random
def cumsum(l):
    t=[]
    m=0
    for i in l:
        m+=i
        t.append(m)
    return t

def help_():
    print("Type set-l for setting the number of integers \nType set-r for setting the range of the integers\nPress enter to generate new list of integers\nPress enter when in triple '>'mode to show cumulative sum\nType 'quit' to quit")

def gen(start,end):
    return random.randint(start,end)

def list_gen(l,start,end):
    m=[]
    for i in range(l):
        i=gen(start,end)
        m.append(i)
    return m




