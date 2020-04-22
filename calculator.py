# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:49:20 2020

@author: NIDA UL HAQ
"""


#Faiza Khan
#Roll No: PIAIC125101
#Batch-9 AI Islamabad
#1st Assignment 22-04-2020
#Calculator 


print("Calculator")

firstnum=int(input("Please Enter your 1st Number:  "))
secondnum=int(input("Please Enter your 2nd Number:  "))

n = input('''Select from following operations to Perform calculation:
\n1 for addition +
2 for subtraction -
3 for division /
4 for multiplication *
\nYou have Entered: ''')

if n == '1':
    print("Addition of "+ str(firstnum)+ " and "+ str(secondnum)+ " is : ",firstnum+secondnum)

elif n == '2':
    print("Subtraction of "+ str(firstnum)+ " and "+ str(secondnum)+ " is : ",firstnum-secondnum)

elif n == '3':
    print("Division of "+ str(firstnum)+ " and "+ str(secondnum)+ " is : ",firstnum/secondnum)

elif n  == "4":
    print("Multiplication of "+ str(firstnum)+ " and "+ str(secondnum)+ " is : ",firstnum*secondnum)
 
elif n  != "1,2,3,4":
    print("You have entered Invalid number. Please Enter Correct Number to Perform operation")    
  
        
   