import random

from apti_library import cumsum
from apti_library import list_gen
from apti_library import help_


def addprac():
    print("Default length:7/nDefault start value: 10/nDefault end value: 100")
    length_of_list = 7
    start= 10
    end = 100


    while(1):

        ip=input(">>")
        tist=list_gen(length_of_list,start,end)
        if ip =="quit":
            break

        elif ip== "set-l":
            length_of_list =int( input("Enter new length "))
            continue
        elif ip== "set-r":
            start= int(input("Enter start value: "))
            end= int(input("Enter end value: "))
            continue

        elif ip=="help_add":
            help_()
            continue

        else:
            print(tist)
            ip2= input(">>>")
            if ip2 == 'n' or ip2 == 'N':
                continue
            else:
                print(cumsum(tist))
