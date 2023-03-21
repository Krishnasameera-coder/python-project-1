#rock paper scissors
import random
def game(computer,you):
    if computer == you:
        return None
    elif computer == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif computer == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif computer == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False

print("computer turn: Rock(r) Paper(p) or scissors(s)")
randno= random.randint(1,3)
if randno==1:
    computer='s'
elif randno==2:
    computer='p'
else:
    computer='s'
you= input("your turn: choose Rock(r) Paper(p) or Scissors(s):")
a = game(computer,you)
print(f"(computer chose {computer})")
print(f"(you choce {you})")
if a==None:
    print("game is a tie!")
elif a:
    print("you win!")
else :
    print("you loose")