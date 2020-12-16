#Put progress notes here. What to do next?
#randomize starting and end location   
#randomize trap location
#add bats
#add arrows
#add wompus
#make wompus harder

import colorama 
from colorama import Fore, Back, Style

mapX = [1,2,3,4,5]
mapY = [1,2,3,4,5]

exitX=5
exitY=5

arrows=10

playerLocationX = 4
playerLocationY = 1

pitX=3
pitY=3

#While player is alive, allow to move
alive = True 

print("player is in room ", playerLocationX, ",", playerLocationY)
while alive:
    #ask player what to do, move, shoot or end game
    action = input("What do you want to do? Move(m), shoot(s), or quit(q)? ")
    if action == "m":
        #ask where to move
        move = input("Where do you want to move (n, s, e, or w) ")
        if move == "n":
            #check for walls
            if playerLocationY+1==6:
                print(Fore.MAGENTA,Back.CYAN, "Oww There is a wall there...",Style.RESET_ALL)
            
            else:
                playerLocationY += 1 

        if move == "s":
            if playerLocationY-1==0:
                print(Fore.MAGENTA,Back.CYAN,"Oww There is a wall there...",Style.RESET_ALL)
            else:   
                playerLocationY -= 1 
        
        if  move == "e":
            if playerLocationX+1==6:
                print(Fore.MAGENTA,Back.CYAN,"Oww There is a wall there...",Style.RESET_ALL)
            else:
                playerLocationX += 1 

        if move == "w":
            if playerLocationX-1==0:
                print(Fore.MAGENTA,Back.CYAN,"Oww There is a wall there...",Style.RESET_ALL)
            else:
                playerLocationX -= 1
            
            
    if action== "s":
        
        if arrows==0:
            print("out of arrows cant shhot anymore")
        else:
            shoot = input(" where do you want to shoot, north(n) south(s) east(e) west(w)")
            print()
            arrows-= 1
            print(Fore.RED,Back.CYAN, "you shoot the arrow and hear a distant thud the arrow hit a wall and shatter",Style.RESET_ALL)
            print("You have ",arrows," arrows remaining")


        #check if fell in a pit. If yes, player dies, game ends
        if playerLocationY==pitY and playerLocationX==pitX:
            alive=False  
            print(Fore.RED,Back.GREEN, "weee it was a fun fall but you hit the bottom and you died", Style.RESET_ALL)
        
        #check if found exit. If yes, player wins, game ends
        if playerLocationX==exitX and playerLocationY==exitY:
            alive=False
            print(Fore.BLUE,Back.YELLOW, "yay you found the exit you feel the breeze and sun on your face", Style.RESET_ALL)
    
    #check if a pit is nearby
    if pitX== playerLocationX+1 and pitY==playerLocationY:
        print(Fore.YELLOW,Back.GREEN,"You hear an echo as if there is a pit nearby", Style.RESET_ALL)
    elif pitX== playerLocationX-1 and pitY==playerLocationY:
        print(Fore.YELLOW,Back.GREEN,"You hear an echo as if there is a pit nearby", Style.RESET_ALL)
    elif pitX== playerLocationX and pitY==playerLocationY+1:
        print(Fore.YELLOW,Back.GREEN,"You hear an echo as if there is a pit nearby", Style.RESET_ALL) 
    elif pitX== playerLocationX and pitY==playerLocationY-1:
        print(Fore.YELLOW,Back.GREEN,"You hear an echo as if there is a pit nearby", Style.RESET_ALL)
    
    #check if the exit is nearby
    if exitX== playerLocationX+1 and exitY==playerLocationY:
        print(Fore.MAGENTA,Back.YELLOW,"you feel a breeze and see a ray of sun, the exit is nearby", Style.RESET_ALL)
    elif exitX== playerLocationX-1 and exitY==playerLocationY:
        print(Fore.MAGENTA,Back.YELLOW,"you feel a breeze and see a ray of sun, the exit is nearby", Style.RESET_ALL)
    elif exitX== playerLocationX and exitY==playerLocationY+1:
        print(Fore.MAGENTA,Back.YELLOW,"you feel a breeze and see a ray of sun, the exit is nearby", Style.RESET_ALL) 
    elif exitX== playerLocationX and exitY==playerLocationY-1:
        print(Fore.MAGENTA,Back.YELLOW,"you feel a breeze and see a ray of sun, the exit is nearby", Style.RESET_ALL)
    

    #end game code
    if action == "q": 
        alive = False
        print("You gave up and died from starvation")


    #for testing, delete for game    
    print("player is in room ", playerLocationX, ",", playerLocationY)

print("The end ")    