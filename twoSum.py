import time
# test case 10^8
testList = [3,3,2]
TARGET = 6

# 從index=0開始找，每次拿出一個數字，找TARGET-List[index]是否存在List中，若有就回傳index，將結果存到new list，最後排序輸出。
# 如果答案是唯一，找到一組就停下來。
timeStart = time.time()
class Solution:
    def twoSum(self, nums, target):
        for Index, Num in enumerate(nums):
            RESIDUE = target - nums[Index]
            if RESIDUE in nums:
                matchIndex = nums.index(RESIDUE)
                if matchIndex != Index:
                    Result = sorted([Index,matchIndex])
                    break

        return Result
        

print(Solution().twoSum(testList,TARGET))

timeEnd = time.time()
timeIntervals = timeEnd - timeStart
if timeIntervals > 2:
    print('超時!!!!!你居然花了', timeIntervals, '秒!!' )
else:
    print('safe!!!!!', '只用掉', timeIntervals, '秒!!', '太棒了~')




