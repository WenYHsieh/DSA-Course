from typing import List
testNums = [-1, 0, 1, 2, -2, -4] 


# 產生出兩兩數字的可能，每次取一對（不重複取），將這兩個數字相加
# 找第三個相加會於0的數字，這數字就是目標值 (前兩個取出的數字和取負): binary search-> 
#                       1. 去除先前取出的兩個數字 2. 將剩下的數字排序 3. 找中間值，把目標值和中間值相比 
#                       4. 若目標值大於中間值就把範圍縮小到目標值右側，反之 5. 在新的一邊找中心點，重複上述比較
#                       6. 若目標值等於中間值，那個數字就是我們要找的。 
class Solution:

    def threeSum(self, nums):
        # 生成所有可能的 index 兩兩排列組合
        indexCombinations = []
        listLength = len(nums)
        for Index1 in range(listLength):
            for Index2 in range(listLength):
                if Index1 != Index2:
                    Conbinations = sorted([Index1, Index2])
                    if Conbinations not in indexCombinations:
                        indexCombinations.append([Index1, Index2])
        
        # Get residual number list and third number
        for IndexPair in indexCombinations:
            ResidualList=[]
            thirdNumber = 0-(nums[IndexPair[0]] + nums[IndexPair[1]])
            #print(IndexPair[0], IndexPair[1])
            #print(thirdNumber)
            for index in range(listLength):
                if index != IndexPair[0] and index != IndexPair[1]:
                    ResidualList.append(nums[index])
            #print(ResidualList)
            
            # Binary search
            outputResult = []
            startIndex = 0
            endIndex = len(ResidualList)-1
    
            if thirdNumber in ResidualList: # 若第三個數字有在數列中，沒有的話 else
                if endIndex >= startIndex:
                    tmpResult = []
                    midIndex =  int((startIndex + endIndex)/2)
                    if ResidualList[midIndex] == thirdNumber:
                        matchIndex = nums.index(ResidualList[midIndex])
                        tmpResult = tmpResult + sorted(IndexPair + [matchIndex])
                        outputResult.append(tmpResult)
                        print(tmpResult)
                    elif thirdNumber > ResidualList[midIndex]:
                        startIndex = midIndex+1
                    else:
                        endIndex = midIndex-1

            else: # 這組就跳過不輸出東西
                print('not found')
                continue
        return outputResult


#Solution().threeSum(testNums)
Solution().threeSum(testNums)
