from typing import Counter, List
class BoardGame:
    def __init__(self, h :int, w :int):
        """
        Set the width and height of the board
        
        Parameters:
            h (int): The height of the board
            w (int): The width of the board
        """
        self.Size = h*w
        self.col = w
        self.row = h
        # UF 維護 connection
        self.Id = list(range(h*w))
        # UF 維護 tree balance
        self.Depth = [1] * h*w
        # BoardGame 維護每下一顆子的index跟類別
        self.Stones = {} # {index:stone type}
        # BoardGame 維護每下一顆子的index跟周長變化: 記錄在self.Stones
        self.Perimeters = {} # {root:perimeter}


    def root(self, i): # 丟 轉換過後的index，得到他屬於哪個CC
        while i != self.Id[i]:
            self.Id[i] = self.Id[self.Id[i]]
            i = self.Id[i]
        return i


    def union(self, p, q): # 丟兩個要union的 轉換後的index (p,q)，做weighted quick unoin
        i = self.root(p)
        j = self.root(q)
        if self.Depth[i] < self.Depth[j]:
            self.Id[i] = j
            self.Depth[j] += self.Depth[i]
        else:
            self.Id[j] = i
            self.Depth[i] += self.Depth[j]

    def xyToIndex(self, x: int, y: int):
        return (x*self.col)+y

    def directionExistance(self, index: int): # 丟一個座標，回傳該座標上下左右存在的index list
        i = int(index/self.col)
        j = index%self.col
        Directions = list(filter(lambda x:x[0] in range(self.row) and x[1] in range(self.col), [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]))
        self.directionIndexs = [self.xyToIndex(x[0],x[1]) for x in Directions]
        return self.directionIndexs

    def putStone(self, x :List[int], y :List[int], stoneType :str):
        """
        Put the stones on (x[0],y[0]), (x[1], y[1]) ...
        
        We grantee that there are not stones at (x[i],y[i]) on the board.
        
        Parameters:
            x (int): The vertical position of the stone, 0 <= x < h
            y (int): The horizotal position of the stone, 0 <= y < w
            stoneType (string): The type of the stones to be put ont the board, which has only two values {'O', 'X'}
        """
        # get index set
        self.Indexs = [self.xyToIndex(x[i], y[i]) for i in range(len(x))]
        # record stone
        self.Stones.update({self.Indexs[i]:stoneType for i in range(len(x))})
        # set all default Perimeter to 4
        self.Perimeters.update({self.root(self.Indexs[i]):4 for i in range(len(x))})

        for index in self.Indexs: # 所有新放進去的stones 一個個拿出來
            avaliableSurrounding = self.directionExistance(index)

            if avaliableSurrounding != []: # 如果上述列表還有東西就要開始查
                rootCheckedList=[]
                for asi in avaliableSurrounding:
                    if asi in self.Stones.keys():# 有放過stone的格子才有紀錄，所以要跳過還沒放過stone的格子不查
                        rootOfASI = self.root(asi) # 再找拿起來比的周邊那顆的root 存著
                        rootCheckedList.append(rootOfASI) 

                        if self.Stones[index] == self.Stones[asi]: # 如果是相同型的 stone
                            if rootCheckedList.count(rootOfASI) == 1:
                                self.union(index, asi)
                                rootOfIndex = self.root(index)  # 把她周圍能夠查詢的方位的index列出來
                                self.Perimeters.update({rootOfIndex:(self.Perimeters[rootOfIndex]+self.Perimeters[rootOfASI])-2})

                            if rootCheckedList.count(rootOfASI) > 1:   
                                rootOfIndex = self.root(index)  # 把她周圍能夠查詢的方位的index列出來
                                self.Perimeters.update({rootOfIndex:self.Perimeters[rootOfIndex]-2})
                        
                        else: # 如果是不同型的 stone
                            rootOfIndex = self.root(index)  # 把她周圍能夠查詢的方位的index列出來
                            self.Perimeters.update({rootOfIndex:self.Perimeters[rootOfIndex]-1}) # 新放的這棵本身要周長-1
                            self.Perimeters.update({rootOfASI:self.Perimeters[rootOfASI]-1}) # 周圍那顆周長也要-1
            else:
                break
            
        return

    def surrounded(self, x :int, y :int) -> bool:
        """
        Answer if the stone and its connected stones are surrounded by 'another type' of stones, which means they are qualified to be flipped if we want.
        
        Parameters:
            x (int): The vertical position of the stone, 0 <= x < h
            y (int): The horizaontal position of the stone, 0 <= y < w
        Returns:
            surrounded (bool): can be flipped of not.
        """
        # return which stone with 0 perimeter
        Index = self.xyToIndex(x,y)
        surrounded = self.Perimeters[self.root(Index)] == 0
        return surrounded

    def getStoneType(self, x :int, y :int) -> str:
        """
        Get the type of the stone at (x,y)
            
        We grantee that there are stones at (x,y)
        
        Parameters:
            x (int): The vertical position of the stone, 0 <= x < h
            y (int): The horizaontal position of the stone, 0 <= y < w
        Returns:
            stoneType (string): The type of the stones, which has only two value {'O', 'X'}
        """
        Index = self.xyToIndex(x,y)
        stoneType = self.Stones[Index]
        return stoneType

# g = BoardGame(3, 3)
# g.putStone([1], [1], 'O')
# print(g.surrounded(1, 1))

# g.putStone([0,1, 1], [1, 0, 2], 'X')
# # print(g.Perimeters)
# print(g.surrounded(1, 1))

# g.putStone([2], [1], 'X')
# print(g.surrounded(1, 1))
# print(g.surrounded(2, 1))

# g.putStone([2], [0], 'O')
# print(g.surrounded(2, 0))
