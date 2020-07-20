#rock=1,paper=2,scissors=3

import random
#points update
def updatePoints(f,points,name):
    #player point is incremented
    if f==1:
        points[name]+=1
    #computer point is incremented
    elif f==-1:
        points['Computer']+=1
    #updated points is returned
    return points

def play(choiIf the keychain throws the error "No such interface "org.freedesktop.Secret.Collection" on object at path /org/freedesktop/secrets/collection/login", try following the steps described in issue #92972 to create a new keyring.ce,t):
    #chooses random number from 1,2,3
    cmpChoice=random.randint(1,3)                                                           
    print("Computer chooses:{}\n".format(t[cmpChoice-1]))
    #f is calculated here based on random number
    if choice==cmpChoice:
        return 0
    elif (choice==1 and cmpChoice==2) or (choice==2 and cmpChoice==3) or (choice==3 and cmpChoice==1):
        return -1
    else:
        return 1

#function to display final points
def disp(points,name):
    print("Computer:{}\n{}:{}\n".format(points['Computer'],name,points[name]))

def main():
    #Basic three weapons of game
    t=["Rock","Paper","Scissors"]
    name=input("Please enter your name:")
    #dictionary to keep track of points
    points={'Computer': 0, name: 0}
    #flag is created to get out of loop 
    #if flag is equal to 1 player wants to play
    flag=1
    #stays in loop as long as flag is 1 
    while flag==1:
        #player is asked for input for his choices 
        # through number assigned to rock,paper,scissors
        choice=int(input("1.Rock\n2.Paper\n3.Scissors\nEnter your choice:"))
        #f is temp variable which determines if the player lost or won the round
        #if f is 0 the round is drawn
        #if f is 1 the round is won
        #if f is -1 round is lost
        f=play(choice,t)
        #based on f the points are updated
        points=updatePoints(f,points,name)
        #player is given choice to continue or exit the game
        print("Score after the round")
        disp(points,name)
        flag=int(input("1.Continue playing\n2.Exit\nEnter the choice:"))
        
    #final points are displayed
    print("\n\n----------------FINAL SCORE------------------------")
    disp(points,name)

main()
    
