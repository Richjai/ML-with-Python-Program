# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 03:43:48 2021

@author: DELL
"""

#--------------------------------Loops----------------------------------------
#-------------For Loop---------------
# for loop is used in case where we need to execute some part of the code until the given condition
# is satisfied. It is better to use for loop if the number of iteration is known in advance.
#It is frequently used to traverse the data structures like list, tuple, or dictionary.
#Example1:
i=0  
for i in range(0,10):
    print(i,end =',')

#Example2:printing the table of the given number
i=1
num = int(input("Enter a number:"))
for i in range(1,11):
    print("%a X %a = %a" %(num,i,num*i))

#Example3:Nested For loop
n = int(input("Enter the number of rows you want to print?"))
i,j=0,0
for i in range(0,n):
    print()
    for j in range(0,i+1):
        print("*",end="")

#Exampl4: Else statement with For loop
for i in range(0,5):
    print(i)
else:print("for loop completely exhausted, since there is no break.")

#------------While Loop-------------
# while loop is to be used in the scenario where we don't know the number of iterations in advance. 
#The block of statements is executed in the while loop until the condition specified in while loop 
#is satisfied. 
#Example1:
i=1;
while i<=10:
    print(i);
    i=i+1;

#Example2:
i=1
number=0

number = int(input("Enter the number?"))
while i<=10:
    print("%a X %a = %a \n"%(number,i,number*i));
    i = i+1;

#Example3:Infinite while loop
var = 1
while var != 2:
    i = int(input("Enter the number?"))
    print ("Entered value is %d"%(i))

while (1):
    print("Hi! we are inside the infinite while loop");

# For loop is ran finite no. of times even if we give only one value
for i in range(0,1):
    print("Hi! we are inside the finite for loop");

#Example4: Using else with while loop
i=1;
while i<=5:
    print(i)
    i=i+1;
else:print("The while loop exhausted");