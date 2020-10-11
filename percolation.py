class Percolation:
    def __init__(self, N):
        """ Create N-by-N grid, with all sites blocked """
        # 2D square array with N^2 component: index -> 0 ~ N^2-1
        # another 2D square array 存default狀態: all blocked -> 在不同的CC 
        self.Size = N
        self.ccGrid = [list(range(N**2))[num:num+N] for num in range(0, len(list(range(N**2))), N)]
        self.defaultStatus = ['X']*N**2
        self.statusGrid = [self.defaultStatus[num:num+N] for num in range(0, N**2, N)]
        self.virtualTop = -1
        self.virtualBottom = N**2

    def open(self, i, j):
        """ Open site (row i, column j) if it is not open already """
        # 若(i, j) 為 'X', status改成 'O'
        row = i
        col = j
        if self.statusGrid[i][j] == 'X':
            self.statusGrid[i][j] = 'O'

        # 搜尋相鄰的O，做union:
            # 取得相鄰CC的id，把 (i, j)的id也變為相同
            # 可能有多個相鄰的O: 按照上下左右的順序去找，(i, j)會是第一個open的id
            # 之後碰到的全部變成前面的id

        Directions = ['top', 'bottom', 'left', 'right']
        directionIndexs = [[i-1,j], [i+1,j], [i, j-1], [i, j+1]] # 上, 下, 左, 右
        directionDict = dict(zip(Directions,directionIndexs))
        self.existDirectionIndexs = list(filter(lambda x: x[0] in range(self.Size) and x[1] in range(self.Size), directionIndexs))
        self.existDirection = [Directions[directionIndexs.index(item)] for item in self.existDirectionIndexs]
        self.surroundingcc = {}
        self.surroundingStatus = {}

        for i in range(len(self.existDirection)): # index
            self.surroundingcc.update({self.existDirection[i]:self.ccGrid[self.existDirectionIndexs[i][0]][self.existDirectionIndexs[i][1]]})
            self.surroundingStatus.update({self.existDirection[i]:self.statusGrid[self.existDirectionIndexs[i][0]][self.existDirectionIndexs[i][1]]})

        # union 
        resDirections = []

        for direction in self.existDirection: 
            if self.surroundingStatus[direction] == 'O':
                # 取得附近Open 格子 的 CC (id)
                self.ccGrid[row][col] = self.surroundingcc[direction]
                resDirections = self.existDirection[self.existDirection.index(direction)+1:len(self.existDirection)]
                break

        if resDirections != []:
            for res in resDirections:
                if self.surroundingStatus[res] == 'O':
                    surroundingXY = directionDict[res]
                    self.ccGrid[surroundingXY[0]][surroundingXY[1]] = self.ccGrid[row][col]

        # if (i, j) in the top row, then conected to virtual top
        # 如果row0 and row N-1 有兩個open，那virtual node的CC為多少?
        if row == 0: 
            self.virtualTop = self.ccGrid[row][col] 
        # if (i, j) in the last row, then conected to virtual bottom
        if row == self.Size-1:
            self.virtualBottom = self.ccGrid[row][col] 


    def isOpen(self, i :int, j :int) -> bool:
        """ Is site (row i, column j) open? """
        # O: open; X: blocked 
        # 查找 (i, j) 是否為O -> 返回 T or F
        return self.statusGrid[i][j] == 'O'

    def isFull(self, i :int, j :int) -> bool:
        """ Is site (row i, column j) full? """
        # 問是否和前 N object 相連 (或和 virtial-top是否相連)?
        return self.ccGrid[i][j] == self.virtualTop

            
    def percolates(self) -> bool:
        """ Does the system percolate? """     
        return self.virtualTop == self.virtualBottom

s = Percolation(5)
s.open(1,1)
print(s.isFull(1, 1)) 
print(s.percolates())
s.open(0,1)
s.open(2,0)
print(s.isFull(1, 1)) 
print(s.isFull(0, 1)) 
print(s.isFull(2, 0)) 
print(s.percolates())
s.open(2,1)
print(s.isFull(1, 1)) 
print(s.isFull(0, 1)) 
print(s.isFull(2, 0)) 
print(s.isFull(2, 1)) 
print(s.percolates())
print(s.ccGrid)