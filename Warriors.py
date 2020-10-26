from typing import List

class Warriors: 
    def warriors(self, strength :List[int], attack_range :List[int]):
        self.STH = strength
        self.RNG = attack_range
        nunberOfWarriors = len(strength)
        ans=[]

        for index in range(nunberOfWarriors):
            leftBound = index-self.RNG[index]
            rightBound = index+self.RNG[index]
            if leftBound<0: 
                leftBound=0
            if rightBound>nunberOfWarriors-1: 
                rightBound= nunberOfWarriors-1
            while self.STH[index] < self.STH[leftBound]:
                leftBound = leftBound+1

            ans.append(leftBound)

            while self.STH[index] < self.STH[rightBound]:
                rightBound = rightBound-1
            ans.append(rightBound)

        return ans

if __name__ == "__main__":
    sol = Warriors()
    print(sol.warriors([11, 13, 11, 7, 15],
                       [ 1,  8,  1, 7,  2]))