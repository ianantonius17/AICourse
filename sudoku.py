import sys
row = 9
col = 9

def readfile(file):
    f = open(file,"r")
    text = f.read().replace('\n','')
    return text

def upload_to_board(text,board):
    r = 0
    c = 0
    for t in text:
        
        temp = int(t)
        board[r][c] = temp
        c = c+1
        c = c%col
        if c == 0:
            r = r+1
    
def availableSpace(board):
    space = []
    
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                space.append([r,c])
    return space


def getVal(board):
    values = [[0] for n in range(81)]
    
    for r in range(row):
        for c in range(col):
            if board[r][c] != 0:
                continue
            else:
                for i in range(10):
                    if validValue(board , i , r ,c):
                        values[c+r*9].append(i)
                
    return values

            
def getMrvBlock(available ,mrv, minCount):
    block =[]
    for i in range(len(available)):
        if mrv[i] == minCount:
            block.append(available[i])
    
    return block

def getDegree(board , spot):
    r = spot[0]
    c = spot[1]
    square_size = [3,3]
    
    square_r = int(r/square_size[0])
    square_c = int(c/square_size[1])
    degree = 0
    
    for i in range(row):
        if i == r:
            continue
        if board[i][c] == 0:
            degree = degree + 1
    
    for j in range(col):
        if i == c:
            continue
        if board[r][i] == 0:
            degree = degree +1
    
    for i in range(square_size[0]):
        for j in range(square_size[1]):
            temp_r = square_r*3 +i
            temp_c = square_c*3+j
            if [temp_r,temp_c] == [r,c]:
                continue
            if board[temp_r][temp_c] == 0:
                degree = degree +1
    
    return degree


def getSpot(board,block):
    degList =[]
    
    for spot in block:
        degree = getDegree(board,spot)
        degList.append(degree)
        
        maximum = max(degList)
        maxSpot =[]
    for i in range(len(degList)):
        val = degList[i]
        if val == maximum:
            return block[i]
            
    return None 


def validValue(board,val,r,c):
    for i in range(row):
        if val == board[r][i]:
            return False
    
    for j in range(col):
        if val == board[j][c]:
            return False
    
    square_r = int(r/3)
    square_c = int(c/3)
    
    for i in range(3):
        for j in range(3):
            if val == board[i+square_r*3][j+square_c*3]:
                return False
    
    return True


def forwardChecking(remainVal , val , r , c):
    
    for i in range(row):
        if i == r:
            continue
        
        temp = remainVal[c+9*i]
        if len(temp) == 1:
            if temp[0] == val:
                return False
    
    for j in range(col):
        if j == c:
            continue
        
        temp = remainVal[r*9+i]
        if len(temp) == 1:
            if temp[0] == val:
                return False
    square_r = int (r/3)
    square_c = int (c/3)
    
    for i in range(3):
        for j in range(3):
            if [square_r*3+i, square_c*3+j] == [r,c]:
                continue
            
            tmp = remainVal[square_c*3+j+(square_r*3+i)*9]
            if len(temp) == 1:
                if temp[0] == val:
                    return False
                
    return True


def solve(board):
    available = availableSpace(board)
    
    if not available:
        return True
    
    remainVal = getVal(board)
    mrv =[]
    
    for space in available:
        mrv.append(len(remainVal[space[0]*row+space[1]]))
    
    minCount = min (mrv)
    block = getMrvBlock(available,mrv,minCount)
    
    if len(block) == 1:
        spot = block[0]
    else:
        spot = getSpot(board,block)
    
    r = spot[0]
    c = spot[1]
    
    values = list(remainVal[c+r*9])
    for val in values:
        if forwardChecking(remainVal,val,r,c):
            board[r][c] = val
            if solve(board):
                return True
            else:
                board[r][c] = 0
    
    return False


def printBoard(board):
    r = 0
    c = 0
    for i in board:
        
        if r%3 == 0:
            print()
            
        for j in i:
            if c%3 ==0:
                print(' ',end="")
            print(j,end="")
            c += 1
        print()
        c = 0
        r += 1
                   

def run(file):
    board =[[0]*col for n in range(row)]
    game = readfile(file)
    upload_to_board(game,board)
    
    if solve(board):
        print("RESULT:")
        printBoard(board)
    else:
        print("Cannot solve the board")


run("sudoku_board2.txt")