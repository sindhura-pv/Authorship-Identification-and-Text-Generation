"""
This code is the front end of a Text generation and Authorship estimation project
Run this code and enter a number based on the functionality you desire
"""
import code as s
n = 1
while n>=1 and n<=4 :
    n = input("Enter your choice: \n 1: Display cross entropy values \n 2: Generate text \n 3: Identify author \n 4: Print number of types and tokens\n")
    n = int(n)
    if n == 1:
        s.modelEntropy()
        
    elif n == 2:
        a = input("Enter story number \n0. Bryant \n 1. Carroll \n 2. Shakespeare \n")  
        s.generateRandomText(a)

    elif n == 3:
        text = input()
        s.identifyAuthor(text)

    elif n == 4:
        s.stats()

