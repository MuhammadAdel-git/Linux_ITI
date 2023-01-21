import time
import os

stars = int(input("Enter number of arrow head stars:  "))
number_of_rotations = int(input("Enter number of arrow rotations: "))
counter = 0

while True:
    
	
    #For Up Arrow
    print()
    for i in range(stars):
        print(" "*(stars*5),end="")
        for j in range(i+1,stars):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        for j in range(i+1):
            print("*",end="")
        print()
    for i in range(0,stars*2,1):
        print(" "*(stars*5),end="")
        print(" "*(stars-1),end="")
        print("*")
    time.sleep(0.1)
    os.system('cls')
    
	
	
    #For Right Arrow
    for i in range(((stars*2)+1)):
        print()
    for i in range(stars):
        if i == (stars-1):
            print(" "*((stars*6)-1),end="");
            print("* "*(2*stars),end="");
            print("* "*(i+1))
        else:
            print(" "*((stars*6)-1),end="");
            print("  "*(2*stars),end="")
            print((i+1)*"* ")
    for j in range(stars-1,0,-1):
        print(" "*((stars*6)-1),end="");
        print("  "*(2*stars),end="")
        print((j)*"* ")
    time.sleep(0.1)
    os.system('cls')

    
	
	#For Down Arrow
    for i in range(stars*3):
        print()
    for i in range(0,stars*2,1):
        print(" "*(stars*5),end="")
        print(" "*(stars-1),end="")
        print("*")
    for i in range(stars):
        print((stars*5)*" ",end="");
        for j in range(i):
            print(" ",end="")
        for j in range(i,stars-1):
            print("*",end="")
        for j in range(i,stars):
            print("*",end="")
        print()
    time.sleep(0.1)
    os.system('cls')

    
	
	#For Left Arrow
    for i in range(((stars*2)+1)):
        print()
    for i in range(stars):
        if i== (stars-1):
            print(" *"*(2*stars),end="");
            print(" *"*(i+1))
        else:
            print("  "*(stars-i-1),end="")
            print((i+1)*" *")
    for j in range(1,stars,1):
        print("  ",end="")
        print((stars-j)*" *")
        print((j)*"  ",end="")
    time.sleep(0.1)
    os.system('cls')
    counter+=1
    if counter==number_of_rotations:
        break