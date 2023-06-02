import random

list = ["stone","paper","scissor"]
score=0
played=0

def winner(userV,compV):
  if userV==compV+1 or userV==compV-2:
    return True
  else:
    return False

def game():
    global played
    global score
    played+=1
    print(list)
    userVal = 0
    try:
      userVal = int(input("Enter index of chosen value: "))
    except:
      print("Enter Integer value")
      game()
      return
    if userVal not in [0, 1, 2]:
      print("Enter index values i.e 0, 1 or 2")
      game()
      return
    compVal = int(random.random()*100 % 3)
    
    print("You selected : "+list[userVal])
    print("Computer selected : "+list[compVal])
    
    if compVal==userVal:
      print('tie lol')
      game()
    elif winner(userVal,compVal):
      print("You won")
      score+=1
    else:
      print("You loose")
      score-=1
while(True):
    game()
    a = input("Enter y to play again: ")
    if(a!='y'):
        break
print(" Thanks for Playing :(" )
print("""
------------------------------------------
Scoreboard
          Games Played: """+str(played)+"""
          Score: """+str(score)+"""
------------------------------------------""")
