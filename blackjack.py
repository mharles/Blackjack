#!/usr/bin/python3
import random
import time

deck = [2, 2, 2, 2, 3 ,3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9 ,9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]
random.shuffle(deck)
value = {"J": 10, "Q": 10, "K": 10, "A": 11}

player = [deck.pop(), deck.pop()]
dealer = [deck.pop(), deck.pop()]
playerbackup = []
dealerbackup = []

playersum = 0
dealersum = 0

def hit(list, sum):
  list.append(deck.pop())
  if type(list[len(list) - 1]) is str:
    sum += value[list[len(list) - 1]]
  else:
    sum += list[len(list) - 1]
  return sum

def show():
  print("#################################################")
  print(f"Dealer shows:  {dealer[0]} ?")
  print(f"Your hand is: {*player,}{*playerbackup,}")
  print(f"Your total is {playersum}.")
  print("#################################################")


def show2():
  print("#################################################")
  print(f"Dealer hand is: {*dealer,}{*dealerbackup,}")
  print(f"Dealer's total is {dealersum}.")
  print(f"Your hand is: {*player,}{*playerbackup,}")
  print(f"Your total is {playersum}.")
  print("#################################################")

def opt():
  o = input("Hit[h]  Stand[s]")
  while o != "h" and o != "s":
    option = input("Hit[h]  Stand[s]")
  return o

playerturn = False
dealerturn = False
gameover = False
option = ""

for i in range (0, 2):
  if type(player[i]) is str:
    playersum += value[player[i]]
  else:
    playersum += player[i]

  if type(dealer[i]) is str:
    dealersum += value[dealer[i]]
  else:
    dealersum += dealer[i]

playerturn = True

show()

while playerturn:
  option = opt()

  if option == "h":
    playersum = hit(player, playersum)

    if playersum > 21:
      for i in range(0, len(player)):
        if player[i] == "A":
          playersum -= 10
          playerbackup.append(player.pop(i))
          break
      if playersum > 21:
        show()  
        print(f"You are busted!")
        playerturn = False
        gameover = True
    else:
      show()

  if option == "s":
    playerturn = False
    dealerturn = True

if gameover == False:   
  show2()

  while dealerturn:
    while dealersum < 17:
      time.sleep(1.5)
      dealersum = hit(dealer, dealersum)
      if dealersum > 21:
        for i in range(0, len(dealer)):
          if dealer[i] == "A":
            dealersum -= 10
            dealerbackup.append(dealer.pop(i))
            break
      show2()
    dealerturn = False

  if dealersum > 21:
    print("Dealer is busted! You win!")
  elif dealersum > playersum:
    print("You lost!")
  elif dealersum < playersum:
    print("You win!")
  else:
    print("It's a push!")   
