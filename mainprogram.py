board= ['-' for i in range(9)]
def displayboard():
    print("|", board[0],"|" ,board[1],"|", board[2])
    print("|" ,board[3],"|" ,board[4],"|", board[5])
    print("|" ,board[6],"|", board[7],"|" ,board[8])
def check_conditions(player):
    conditions= [
        [0,1,2],[2,4,5],[6,7,8],[0,3,6],
        [1,4,7],[2,5,8],[0,4,8],[2,4,6],
     ]
    for check in conditions:
             if board[check[0]] == player and board[check[1]] == player and board[check[2]] == player:
                 return 1
    else:
            return 0
player1= "x"
player2= "o"
def startgame():
    while True:
        while True:
            player1_option= input(f"{player1}',Enter your position:")
        if player1_option not in [str(i) for i in range(1,10)]:
            print("please enter [1-9]")
            continue
        if board[int(player1_option)-1] == "-":
           board[int(player1_option)-1] = player1
           displayboard()
           if check_conditions(player1):
               return f'winner :{player1}'
        break
    else:
            print("this place is not empty")
while True:
        player2_option= input(f"{player2}',Enter your position:")
        if player2_option not in [str(i) for i in range(1,10)]:
            print("please enter [1-9]")
            continue
        if board[int(player2_option)-1] == "-":
                  board[int(player2_option)-1] = player2
                  displayboard()
                  if check_conditions(player2):
                     return f'winner :{player2}'
                 break
else:
                print("this place is not empty")


print(startgame())
while True:
    play_again= input("Do u want to play again [Y/y]:")
    if play_again in "Y/y":
           board = ['-' for i in range(9)]
           print(startgame())
else:
        exit()
            


