
testNums =  [-1, 0, 1, 2, -2, -4]


# 產生出兩兩數字的可能，每次取一對（不重複取），將這兩個數字相加
# 找第三個相加會於0的數字，這數字就是目標值 (前兩個取出的數字和取負): binary search-> 
#                       1. 去除先前取出的兩個數字 2. 將剩下的數字排序 3. 找中間值，把目標值和中間值相比 
#                       4. 若目標值大於中間值就把範圍縮小到目標值右側，反之 5. 在新的一邊找中心點，重複上述比較
#                       6. 若目標值等於中間值，那個數字就是我們要找的。 
# linear search v1 #
from typing import List
class Solution:
    def Combinations(self, nums):
    # 生成所有可能的 數列中數字 兩兩排列組合
        allCombinations = []
        for Num1 in nums:
            for Num2 in nums:
                if Num1 != Num2:
                    Combns = sorted([Num1, Num2])
                    if Combns not in allCombinations:
                        allCombinations.append(Combns)
        return allCombinations

    def threeSum(self, nums):
        pairwiseNums = self.Combinations(nums)
        outputResult = []
        # Get residual number list and third number
        for Pair in pairwiseNums:
            ResidualList=[]
            thirdNumber = 0-(Pair[0] + Pair[1])
            #print(Pair[0], Pair[1])
            for Num in nums:
                if Num != Pair[0] and Num != Pair[1]:
                    ResidualList.append(Num)
            #print(ResidualList)

            if thirdNumber in ResidualList:
                tmp = sorted(Pair+[thirdNumber])
                if tmp not in outputResult:
                    # print(tmp)
                    outputResult.append(tmp)
        return outputResult

# binary search  v2 #

from typing import List
class Solution:

    def binarySearch(self, resNumsList, residual):
        # residual list: sorted
        startIndex = 0
        endIndex = len(resNumsList)-1
        while(endIndex >= startIndex):
            midIndex = int((startIndex+endIndex)/2)

            if residual == resNumsList[midIndex]:
                return midIndex
            elif residual > resNumsList[midIndex]:
                startIndex = midIndex+1
            else:
                endIndex = midIndex-1
        return 


    def threeSum(self, nums):
        allCombinations = []
        for Num1 in nums:
            for Num2 in nums:
                if Num1 != Num2:
                    Combns = sorted([Num1, Num2])
                    if Combns not in allCombinations:
                        allCombinations.append(Combns)

        outputResult = []
        # Get residual number list and third number
        for Pair in allCombinations:
            Residual = 0-(Pair[0] + Pair[1])
            residualList = sorted([num for num in nums if num != Pair[0] and num != Pair[1]])
            matchIndex = self.binarySearch(residualList, Residual)
            if matchIndex != None:
                tmp = sorted(Pair + [residualList[matchIndex]])
                if tmp not in outputResult:
                    outputResult.append(tmp)
        return outputResult

print(Solution().threeSum(testNums))

