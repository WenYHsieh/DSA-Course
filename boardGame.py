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


    def find(self, p, q): # 丟兩個轉換後的index (p,q) 回傳他們是否在同個CC
        return self.root(p) == self.root(q)

    def xyToIndex(self, x: int, y: int):
        return (x*self.col)+y
    def directionExistance(self, index: int): # 丟一個座標，回傳該座標上下左右存在的index list
        #Directions = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
        i = int(index/self.Size)
        j = index%self.Size
        directionIndexs = [self.xyToIndex(i-1,j), self.xyToIndex(i+1,j), self.xyToIndex(i,j-1), self.xyToIndex(i,j+1)]
        existDirectionIndexs = list(filter(lambda x: x in range(self.Size**2), directionIndexs)) 
    
        return existDirectionIndexs

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
        Indexs = [self.xyToIndex(x[i], y[i]) for i in range(len(x))]
        # record stone
        self.Stones.update({Indexs[i]:stoneType for i in range(len(x))})
        # set all Perimeter to 4
        self.Perimeters.update({self.root(Indexs[i]):4 for i in range(len(x))})
        Counter = 0
        for index in Indexs:
            avaliableSurrounding = self.directionExistance(index)
            if avaliableSurrounding == []:
                break
            for asi in avaliableSurrounding:
                p = self.root(index)
                q = self.root(asi)

                if self.Stones[index] == self.Stones[asi]: # 如果是相同型的 stone
                    if q == asi: # 如果周圍的那個是自成一組
                        self.union(index, asi)
                        self.Perimeters.update({self.root(index):self.Perimeters[p]+4-2})
                    if q != asi and Counter == 0:  # 如果周圍的那個並非自成一組
                        self.union(index, asi)
                        self.Perimeters.update({self.root(index):self.Perimeters[p]+4-2})
                        Counter+=1
                    if q != asi and Counter != 0: # 如果周圍的那個並非自成一組，而且不是第一次查到這組
                        self.union(index, asi)
                        self.Perimeters.update({self.root(index):self.Perimeters[p]-2})
                        Counter+=1

                else: # 如果是不同型的 stone
                    self.Perimeters.update({self.root(index):self.Perimeters[p]-1})
            
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

g = BoardGame(3, 3)
g.putStone([1], [1], 'O')
print(g.surrounded(1, 1))