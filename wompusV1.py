import colorama 
from colorama import Fore, Back, Style

mapX = [1,2,3,4,5]
mapY = [1,2,3,4,5]

exitX=5
exitY=5

playerLocationX = 4
playerLocationY = 1

pitX=3
pitY=3

alive = True 

print("player is in room ", playerLocationX, ",", playerLocationY)
while alive:
    move = input("Where do you want to move (n, s, e, or w)")
    if move == "n":
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

    if playerLocationY==pitY and playerLocationX==pitX:
        alive=False  
        print(Fore.RED,Back.GREEN, "weee it was a fun fall but you hit the bottom and you died", Style.RESET_ALL)

    if playerLocationX==exitX and playerLocationY==exitY:
        alive=False
        print(Fore.BLUE,Back.YELLOW, "yay you found the exit you feel the breeze and sun on your face", Style.RESET_ALL)
    
    print("player is in room ", playerLocationX, ",", playerLocationY)

print("The end ")    