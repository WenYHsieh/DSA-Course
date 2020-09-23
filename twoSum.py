
# nums = list(range(1000))
# target = 1997

# hash table 的使用 

from typing import List
class Solution:
    def twoSum(self, nums, target):
        hashTable={}
        for index, num in enumerate(nums):
            Residual = target - num
            if hashTable.__contains__(Residual):
                Result = [hashTable.get(Residual), index] # index 一定大於 Residual ，因為 Residual 是從已經建立的 hashtable找，因此不用排序
                break
            else: # 邊搜尋邊建立: {num:index}
                hashTable[num]=index 

        return Result
        


#print(Solution().twoSum(nums,target))
