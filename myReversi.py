import random
import copy
row  = col = 8
badPos = [[1,1],[1,6],[6,1],[6,6]]
priorityPos = [[0,0],[0,7],[7,0],[7,7]]
black = 'b'
white = 'w'
enemyColor = black
depth = 4

def checkBelow(board,color,r,c):
    count = 0
    for i in range(col):
        if i == 0:
            continue
        if r+i >= row :
            break
        if board[r+i][c] == None:
            break
        if board[r+i][c] == color:
            if count == 0:
                return False
            return True
        
        count += 1
        
    return False

def checkAbove(board,color,r,c):
    count = 0
    for i in range(col): 
        if i == 0:
            continue
        if r-i < 0 :
            break
        if board[r-i][c]==None:
            break
        if board[r-i][c] == color:
            if count == 0:
                return False
            return True
        
        count += 1
    
    return False
    
def checkCol(board,color,r,c):
    above = checkAbove(board,color,r,c)
    below = checkBelow(board,color,r,c)
   # print('a',a , 'b',b)

    return above or below
    
#works
def checkRight(board,color,r,c):
    count = 0
    for i in range(col):
        if i == 0:
            continue
        if c+i >= col :
            break
        if board[r][c+i] == None:
            break
        if board[r][c+i] == color :
            if count == 0 :
                return False
            return True
        
        count += 1
    return False

def checkLeft(board,color,r,c):
    count = 0
    for i in range(col):
        if i == 0:
            continue
        if c-i < 0 :
            break
        if board[r][c-i]== None:
            break
        if board[r][c-i] == color:
            if count == 0:
                return False
            return True
        count += 1
        
    return False

def checkRow(board,color,r,c):
    right = checkRight(board,color,r,c)
    left = checkLeft(board,color,r,c)
    #print('r',rt , 'l',lt)

    return right or left

def checkBottomRight(board,color,r,c):
    count = 0
    for i in range(row): 
        if i == 0 :
            continue
        if r+i >= row or c+i >= col:
            break
        if board[r+i][c+i]==None:
            break
        if board[r+i][c+i] == color:
            if count == 0 :
                return False
            return True
        count += 1
    return False
    
def checkTopRight(board,color,r,c):
    count = 0
    for i in range (row):
        if i == 0 :
            continue
        if r-i < 0 or c+i >= row:
            break
        if board[r-i][c+i]==None:
            break
        if board[r-i][c+i] == color:
            if count == 0:
                return False
            return True
        count += 1
    return False
    
def checkBottomLeft(board,color,r,c):
    count = 0
    for i in range(row):
        
        if i == 0:
            continue
        if r+i >= row or c-i < 0 :
            break
        if board[r+i][c-i]==None:
            break
        if board[r+i][c-i] == color:
            if count == 0:
                return False
            return True
        count += 1
    return False
    
def checkTopLeft(board,color,r,c):
    count = 0
    for i in range(row):
        if i == 0:
            continue
        if r-i < 0 or c-i < 0:
            break
        if board[r-i][c-i]==None:
            break
        if board[r-i][c-i] == color:
            if count == 0 :
                return False
            return True
        count += 1
            
    return False

def checkDiagonal(board,color,r,c):
    botRight = checkBottomRight(board,color,r,c)
    botLeft = checkBottomLeft(board,color,r,c)
    topRight = checkTopRight(board,color,r,c)
    topLeft = checkTopLeft(board,color,r,c)
    
    #print('br',br,'bl',bl,'tr',tr,'tl',tl)
    
    return botRight or botLeft or topRight or topLeft
    
def validSpot(board,color,r,c):
    rw = checkRow(board,color,r,c)
    #print ('r',r)
    cl = checkCol(board,color,r,c)
   # print ('c',c)
    dg = checkDiagonal(board,color,r,c)
   # print ('d',d)
    return rw or cl or dg

def getAvailableSpot(board,color):
    available = []
    for i in range(row):
        for j in range(col):
            if board[i][j] != None:
                continue
            #print(i,j)
            if validSpot(board,color,i,j) == True:
                spot = [i,j]
                #print(spot)
                available.append(spot)
                
    return available

#get available direction to flip the beads 
#direction get in clockwise started from moving above is equal to 1
def getDirection(board,color,r,c):
    dir =[]
    if checkAbove(board,color,r,c):
        dir.append(1)
    if checkTopRight(board,color,r,c):
        dir.append(2)
    if checkRight(board,color,r,c):
        dir.append(3)
    if checkBottomRight(board,color,r,c):
        dir.append(4)
    if checkBelow(board,color,r,c):
        dir.append(5)
    if checkBottomLeft(board,color,r,c):
        dir.append(6)
    if checkLeft(board,color,r,c):
        dir.append(7)
    if checkTopLeft(board,color,r,c):
        dir.append(8)
    return dir

def flip(board,color,r,c):
    direction = getDirection(board,color,r,c)
    #flip beads above
    if 1 in direction:
        for i in range(row):
            if i == 0:
                continue
            if r-i < 0:
                break
            if board[r-i][c] == color or board[r-i][c] == None:
                break
            board[r-i][c] = color
        
    #flip beads top right
    if 2 in direction:
        for i in range(row):
            if i == 0:
                continue
            if r-i < 0 or c+i >= col:
                break
            if board[r-i][c+i] == color or board[r-i][c+i] == None:
                break
            board[r-i][c+i] = color
        
    #flip beads right
    if 3 in direction:
        for i in range(row):
            if i == 0:
                continue
            if c+i >= row:
                break
            if board[r][c+i] == color or board[r][c+i] == None:
                break
            board[r][c+i] = color
    #flip beads bottom right
    if 4 in direction:
        for i in range(row):
            if i == 0 :
                continue
            if r+i >= row or c+i >= row:
                break
            if board[r+i][c+i] == color or board[r+i][c+i] == None:
                break
            board[r+i][c+i] = color
    
    #flip beads below
    if 5 in direction:
        for i in range(row):
            if i == 0:
                continue
            if r+i >= row:
                break
            if board[r+i][c] == color or board[r+i][c] == None:
                break
            board[r+i][c] = color
    
    #flip beads bottom left
    if 6 in direction:
        for i in range(row):
            if i == 0 :
                continue
            if r+i >= row or c-i < 0:
                break
            if board[r+i][c-i] == color or board[r+i][c-i] == None:
                break
            board[r+i][c-i] = color
    
    #flip left
    if 7 in direction:
        for i in range(row):
            if i == 0 :
                continue
            if c-i < 0 :
                break
            if board[r][c-i] == color or board[r][c-i] == None:
                break
            board[r][c-i] = color
    
    #flip top left
    if 8 in direction:
        for i in range(row):
            if i == 0 :
                continue
            if r-i < 0 or c-i < 0:
                break
            if board[r-i][c-i] == color or board[r-i][c-i]==None:
                break
            board[r-i][c-i] = color

def placeBeads(board,color,r,c,availableSpots):
    if [r,c] not in availableSpots:
        return False
    board[r][c] = color
    flip(board,color,r,c)
    return True

def finished(board):
    x =0
    y =0
    z =0
    
    for line in board:
        if black in line:
            x = 1
        if white in line:
            y = 1
        if None in line:
            z = 1
       
    if x+y+z == 3:
        return False
        
    
    return True

#black will always make the first move
def printBoard(board):
    for i in range(row):
        for j in range(col):
            print("|",end="")
            
            if board[i][j] == None:
                print("_",end="")
            else:
                print(board[i][j],end="")
        print("|")
                
    
def play(board,color,level):
    if color == black:
        my = black
        #enemy = white
        myTurn = True
    else:
        my = white
        #enemy = black
        myTurn = False
    
    blackTurn = True
    while not finished(board):
       # print("----------------------------")
        #printBoard(board)
        if blackTurn :
            message = "Black's"
            clr = black
        else:
            message = "White's"
            clr = white
        #print(message,"Turn")
        availSpots = getAvailableSpot(board,clr)
        if not availSpots:
            if not getAvailableSpot(board,white) and not getAvailableSpot(board,black):
                break
            print(message.strip("'s'"),"has no available move")
            blackTurn = not blackTurn
            myTurn = not myTurn
            continue
        while True:
            
            #print("Available Spots:")
            #for x in availSpots:
            #    print('[', x[0]+1, ',', x[1]+1, ']')
            if myTurn:   
                #print("row:")
                #rowInput = int(input())-1
                #print("column:")
                #colInput = int(input())-1
                spot = dumbBot(availSpots)
                rowInput = spot[0]
                colInput = spot[1]
                #rowInput,colInput = bestMove(board,clr,availSpots)
            else:
                rowInput,colInput = bestMove(board,clr,availSpots,level)
            
            if placeBeads(board,clr,rowInput,colInput,availSpots):
                blackTurn = not blackTurn
                myTurn = not myTurn
                break
            else:
                print("Invalid spot ! Please re-input your spot")
    #printBoard(board)
    print("Game has Ended")
    evaluate(board,my)
    


def getScore(board,color):
    counter = 0
    for line in board:
        for pos in line:
            if pos == color:
                counter += 1
                
    return counter

def countScore(board,color):
    #max score is 100
    cnt = 0
    for r in range(row):
        for c in range(col):
            if board[r][c] == color:
                if (r==0 or r==row-1) and (c==0 or c==col-1):
                    cnt += 4
                elif r==0 or r==row-1 or c==0 or c==col-1:
                    cnt += 2
                elif (r == 1 or r == row-1) and(c==1 or c == col-1):
                    cnt -= 8
                else:
                    cnt += 1
    return cnt

def evaluate(board, my):
    whiteScore = 0
    blackScore = 0
    for i in range(row):
        for j in range(col):
            if board[i][j] == white:
                whiteScore += 1
            if board[i][j] == black:
                blackScore += 1
    if my == black:
        print("White Score(AI): ", whiteScore)
        print("Black Score (Player): ", blackScore)
    else:
        print("White Score(Player): ", whiteScore)
        print("Black Score (AI): ", blackScore)

def chooseColor(): 
    while True:
        print("Choose your color (black or white) : ",end="")
        userInput = str(input()).lower()
        #userInput ='black'
        if 'black' in userInput:
            choosenColor = black
            break
        elif 'white' in userInput:
            choosenColor = white
            break
        else:
            print("You did not choose the right color")
        
    return choosenColor
def chooseLevel():
    while True:
        print("Choose your desired level of difficulty (Easy/Medium/Hard) : ")
        userInput = str(input()).lower()
        #userInput = 'hard'
        if "easy" in userInput:
            depth = 2
            level = "easy"
            break
        elif "medium" in userInput:
            depth = 8
            level = "medium"
            break
        elif "hard" in userInput:
            depth = 20
            level = "hard"
            break
        else :
            print("You did not choose the right difficulty")
    return level   

minEvalBoard = -1
maxEvalBoard = 101

def eliminateBadPos(moves):
    tempMoves = copy.deepcopy(moves)
    for bad in badPos:
        if bad in tempMoves:
            tempMoves.remove(bad)
    if len(tempMoves) > 0:
        moves = tempMoves
    return moves

def priorityMove(moves):
    tempMoves = copy.deepcopy(moves)
    tempPriority = []
    for priority in priorityPos:
        if priority in moves:
            tempPriority.append(priority)
    if len(tempPriority)>0:
        moves = tempPriority
    return moves

def dumbBot(availableSpot):
    if len(availableSpot) == 0:
        return None
    if len(availableSpot) == 1:
        return availableSpot[0]
    index = random.randint(0,len(availableSpot)-1)
    return availableSpot[index]
#MINIMAX
def minimax(board, color, depth, maximize):
    if depth == 0:
        return #score
    moves = getAvailableSpot(board,color)
    if maximize:
        bestVal = minEvalBoard
        for move in moves:
            tempRow = move[0]
            tempCol = move[1]
            copyBoard = copy.deepcopy(board)
            if placeBeads(copyBoard, color, tempRow, tempCol, move):
                tempRow,tempCol,val = minimax(copyBoard, color, depth-1, False)
                bestVal = max(bestVal, val)
            
    else:
        #minimize player
        bestVal = maxEvalBoard
        for move in moves:
            tempRow = move[0]
            tempCol = move[1]
            copyBoard = copy.deepcopy(board)
            if placeBeads(copyBoard, color, tempRow, tempCol, move):
                tempRow,tempCol,val = minimax(copyBoard, color, depth-1, True)
                bestVal = min(bestVal, val)
    return tempRow,tempCol,bestVal

#MINIMAX WITH ALPHA BETA PRUNING
def alphaBeta(board, color, depth,level, alpha, beta,rowInput,colInput ,maximize):
    if depth == 0:
        return rowInput,colInput,countScore(board,color)#score
    moves = getAvailableSpot(board,color)
    #eliminate bad spot
    if level =="medium" or level =="hard":
        moves = eliminateBadPos(moves)
    
    if level =="hard":
        moves = priorityMove(moves)
    
    if maximize:
        #val = minEvalBoard
        #print("MAX")
        val = beta
        for move in moves:
            #print("WOWMAX")
            tempR = move[0]
            tempC = move[1]
            copyBoard = copy.deepcopy(board)
            r,c,pruning = alphaBeta(copyBoard, color, depth-1,level, alpha, beta,rowInput,colInput, False)
            val = max(val,pruning )
            alpha = max(alpha, val)
            if alpha == pruning:
                tempR = r
                tempC = c
                #print("YES")
            if alpha >= beta:
                #print("BREAK1")
                break
        
    else:
        #minimize player
        #val = maxEvalBoard
        #print("MIN")
        val = alpha
        for move in moves:
            #print("WOW")
            tempR = move[0]
            tempC = move[1]
            copyBoard = copy.deepcopy(board)
            r,c,pruning = alphaBeta(copyBoard, color, depth-1,level, alpha, beta,rowInput,colInput, True)
            val = min(val, pruning)
            beta = min(beta, val)
            if beta == pruning:
                tempR = r
                tempC = c
               # print("NO")
            if alpha >= beta:
                #print("BREAK2")
                break
    return tempR,tempC,val

def bestMove(board,color, moves,level):
    #moves = getAvailableSpot(board,color)
    tempPoint = 0
    x = moves[0][0]
    y = moves[0][1]
    for move in moves:
        rowInput = move[0]
        colInput = move[1]
        #rowInput = 0
        #colInput = 0
        copyBoard = copy.deepcopy(board)
        rowInput,colInput,point = alphaBeta(copyBoard, color, depth,level, minEvalBoard, maxEvalBoard,rowInput,colInput ,True)
        #rowInput,colInput,point = minimax(copyBoard,color,depth,True)
        if point > tempPoint:
            #print("Hi")
            tempPoint = point
            x = rowInput
            y = colInput
            #print(x,y,point)
    return (x,y)

def main():
    
    #Initialization
    board = [[None]*col for n in range(row)]
    board[4][4] = black
    board[3][3] = black
    board[3][4] = white
    board[4][3] = white
    level =chooseLevel()
    userColor = chooseColor()
    play(board,userColor,level)
for i in range(10):
    main()