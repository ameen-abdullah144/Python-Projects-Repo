def sum(a,b,c):
    return a+b+c

def printInstructions():
    print("Welcome to Tic Tac Toe!")
    print("Instructions:")
    print("1. Player X goes first, followed by Player O.")
    print("2. Choose a number (0-8) to place your mark on the board.")
    print("3. The first to get 3 in a row (horizontally, vertically, or diagonally) wins.")
    print("4. If all 9 squares are filled and no one wins, it's a draw.")
    print("\nBoard Layout:")
    print(" 0 | 1 | 2 ")
    print("---|---|---")
    print(" 3 | 4 | 5 ")
    print("---|---|---")
    print(" 6 | 7 | 8 ")
    print("Good luck!\n")

def printBoard(xState,zState):
    zero= 'X' if xState[0] else ('O'if zState[0] else 0)
    one= 'X' if xState[1] else ('O'if zState[1] else 1)
    two= 'X' if xState[2] else ('O'if zState[2] else 2)
    three= 'X' if xState[3] else ('O'if zState[3] else 3)
    four= 'X' if xState[4] else ('O'if zState[4] else 4)
    five= 'X' if xState[5] else ('O'if zState[5] else 5)
    six= 'X' if xState[6] else ('O'if zState[6] else 6)
    seven= 'X' if xState[7] else ('O'if zState[7] else 7)
    eight= 'X' if xState[8] else ('O'if zState[8] else 8)
    print(f' {zero} | {one} | {two} ')
    print(f'---|---|---')
    print(f' {three} | {four} | {five} ')
    print(f'---|---|---')
    print(f' {six} | {seven} | {eight} ')

def checkWin(xState,zState):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xState[win[0]],xState[win[1]],xState[win[2]])==3):
            print("X won the Match")
            return 1
        if(sum(zState[win[0]],zState[win[1]],zState[win[2]])==3):
            print("O won the Match")
            return 0
        if all(xState[i] == 1 or zState[i] == 1 for i in range(9)):
            print("It's a Draw!")
            return 2
        return -1
    
if __name__=="__main__":
    printInstructions()
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn=1  #1 for X and 0 for O
    # print("Welcome to Tic Tac Toe")
    while(True):
        # printBoard(xState,zState)
        if turn == 1:
            print("X's Chance! ")
            value = int(input('Please enter a value: '))
            xState[value]= 1
        else:

            print("O's Chance! ")
            value = int(input('Please enter a value: '))
            zState[value]= 1
        cwin=checkWin(xState,zState)
        if(cwin !=-1):
                # printBoard(xState,zState)
                print("Game Over")
                break
        printBoard(xState,zState)
        turn = 1- turn

