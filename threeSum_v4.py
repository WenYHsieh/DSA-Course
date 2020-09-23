# two pointer: from leetcode ~ N^2
from typing import List
class Solution:
    def threeSum(self, nums):
        nums.sort()
        numsLength = len(nums)
        Result = []
        for index in range(numsLength):
            if index>0 and nums[index] == nums[index-1]: #?
                continue
            lowIndex = index+1
            highIndex = numsLength-1
            Residual = 0-nums[index]
            while lowIndex < highIndex:
                if nums[lowIndex] + nums[highIndex] < Residual:
                    lowIndex+=1
                elif nums[lowIndex] + nums[highIndex] > Residual:
                    highIndex-=1
                else: # 等於
                    tmp = sorted([nums[lowIndex], nums[highIndex], nums[index]])
                    Result.append(tmp)
                    while lowIndex < highIndex and nums[lowIndex] == nums[lowIndex+1]:
                        lowIndex+=1
                    while lowIndex < highIndex and nums[highIndex] == nums[highIndex-1]:
                        highIndex-=1
                    lowIndex+=1
                    highIndex-=1
        return Result


# nums =  [-1, 0, 1, 2, -2, -4]

# print(Solution().threeSum(nums))
