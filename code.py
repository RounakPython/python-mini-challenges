# --------------
#Code starts here
import sys

def rev_num(n):
        rev=0
        while(n>0):
            rem=n%10
            rev=(rev*10)+rem
            n=n//10
        return rev

def palindrome(num):
    for i in range(num+1, sys.maxsize):
        if(i == rev_num(i)):
            return i


# --------------
#Code starts here
import numpy as np

def convert_touniquelist(string):
    list_0=[]
    for i in string:
        list_0.append(i)
    arr=np.array(list_0)
    return list(arr)

def a_scramble(str_1, str_2):
    x = convert_touniquelist(str_1.lower())
    y = convert_touniquelist(str_2.lower())
    flag = False
    for i in y:
        if i not in x:
            return False
        else:
            x.remove(i)
            flag = True
    return flag
    

a_scramble("baby shower","shows")
#a_scramble("Tom Marvolo Riddle","Voldemort")
#a_scramble("ticket","chat")


# --------------

#Importing header files
from math import sqrt

#Code starts here
def isPerfectSquare(x): 
    s = int(sqrt(x)) 
    return s*s == x

def check_fib(num): 
    return isPerfectSquare(5*num*num + 4) or isPerfectSquare(5*num*num - 4)


# --------------
#Code starts here
def compress(word):
    list_1=[]
    n=''
    output=''
    c=0
    for i in word.lower():     
        if(i==n):
            c+=1
            list_1[-1]=c
        else:
            n=i
            c=1
            list_1.append(i)
            list_1.append(c)
    for j in list_1:
        output += str(j)
        #print(j,end='')
    return output

compress('Ss')
compress('ssggtts')
compress('banana')


# --------------
#Code starts here
import numpy as np

def k_distinct(string, k):
    ls=[]
    string=(string.lower())
    for i in string:
        ls.append(i)
    x = np.array(ls)
    #print(np.unique(x))
    if len(np.unique(x))==k:
        return True
    else:
        return False


