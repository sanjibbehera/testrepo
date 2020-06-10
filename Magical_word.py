##################################################################################################
#### HackerEarth program to be executed like below:-
#### python Magical_word.py
#### First Input denotes the number of testcases.
#### Second Input denotes the maximum no of letters in the word.
#### Output desired:-
#### Final Output: String closest to magical word.
####################################################################
#### PROBLEM STATEMENT #############################################
#### Dhananjay has recently learned about ASCII values.He is very fond of experimenting. With his knowledge of ASCII values and character he has developed a special word and named it Dhananjay's Magical word.
####
#### A word which consist of alphabets whose ASCII values is a prime number is an Dhananjay's Magical word. An alphabet is Dhananjay's Magical alphabet if its ASCII value is prime.
#### 
#### Dhananjay's nature is to boast about the things he know or have learnt about. So just to defame his friends he gives few string to his friends and ask them to convert it to Dhananjay's Magical word. None of his friends would like to get insulted. Help them to convert the given strings to Dhananjay's Magical Word.
#### 
#### Rules for converting:
#### 
#### 1.Each character should be replaced by the nearest Dhananjay's Magical alphabet.
#### 
#### 2.If the character is equidistant with 2 Magical alphabets. The one with lower ASCII value will be considered as its replacement.
#### 
#### Input format:
#### 
#### First line of input contains an integer T number of test cases. Each test case contains an integer N (denoting the length of the string) and a string S.
#### 
#### Output Format:
#### 
#### For each test case, print Dhananjay's Magical Word in a new line.
##################################################################################################
import sys
from bisect import bisect

no_of_tcs = input()
lines = []
finalarr = []

def getPrimes(limit):
    MAX=1001
    p=2
    prime=[True]*(MAX+1)
    prime[0]=prime[1]=False
    primelist=[]
    while p*p<=MAX:
        if prime[p]:
            for i in range(p*p,MAX+1,p):
                prime[i]=False
        p=p+1
    for i in range(2,MAX+1):
        if prime[i]:
            primelist.append(i)

    # Return the list of prime numbers
    return primelist

for tc in range(int(no_of_tcs)):
    string_length = input()
    strg = input()
    if(len(strg) == int(string_length)):
        lines.append(strg)
    else:
        sys.exit()

for i in range(0, len(lines)):
    word = lines[i]
    for j in range(0, len(word)):
        findAsciiVal = ord(word[j])
        findprimeVal = getPrimes(findAsciiVal)
        ind=bisect(findprimeVal, int(findAsciiVal))
        a=findAsciiVal - findprimeVal[ind - 1]
        b=findprimeVal[ind] - findAsciiVal
        if a<=b:
            #print('Nearest prime no. for letter ', word[j], 'aaaa', findprimeVal[ind-1])
            x = chr(findprimeVal[ind-1])
            finalarr.append(x)
        else:
            #print('Nearest prime no. for letter ', word[j],'bbbb', findprimeVal[ind])
            y = chr(findprimeVal[ind])
            finalarr.append(y)

finalStr = ""
finalStr = ''.join(finalarr)

print(finalStr)