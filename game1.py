player1 = input("PLAYER1: A=ROCK B=PAPER C=SCISSORS")
print ("PLAYER1 HAVE SELECTED: ", player1)
player2 = input("PLAYER2: A=ROCK B=PAPER C=SCISSORS")
print ("PLAYER2 HAVE SELECTED: ", player2)


result = []
a = ("a")
b = ("b") 
c = ("c") 
A = ("A")
B = ("B")
C = ("C")
a = A
b = B
c = C

if player1 == player2:
    print ("TIE")

elif player1 == a and player2 == b:
    print ("PLAYER2 WINS")  
elif player1 == b and player2 == a:
    print ("PLAYER1 WINS")

elif player1 == b and player2 == c:
    print ("PLAYER2 WINS")
elif player1 == c and player2 == b:
    print ("PLAYER1 WINS")
  
elif player1 ==  a and player2 == c:
    print ("PLAYER1 WINS")    
elif player1 == c and player2 == a:
    print ("PLAYER2 WINS")
