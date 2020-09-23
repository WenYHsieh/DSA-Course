# pairwise + binary search ~ N^2lgN
# 1. 數列排序
# 2. 兩兩取出
# 3. 計算residual
# 4. 丟進binary search裡面找
# 5. 返還第三數


from typing import List
class Solution:
    def threeSum(self, nums):
        nums.sort()
        numsLength = len(nums)
        Result = []
        for i in range(0, numsLength):
            for j in range(i+1, numsLength):
                #print(nums[i], nums[j])
                Residual = 0-(nums[i]+nums[j]) 
                startIndex = j+1
                endIndex = len(nums)-1
                while(endIndex >= startIndex):
                    midIndex = int((startIndex+endIndex)/2)
                    if Residual == nums[midIndex]:
                        tmp = [nums[i],nums[j],nums[midIndex]]
                        Result.append(tmp)
                        break
                    elif Residual > nums[midIndex]:
                        startIndex = midIndex+1
                    else:
                        endIndex = midIndex-1

        return Result



nums =  [-1, 0, 1, 2, -2, -4]

print(Solution().threeSum(nums))

