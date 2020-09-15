testList = [3,3]
TARGET = 6

# 從index=0開始找，每次拿出一個數字，找TARGET-List[index]是否存在List中，若有就回傳index，將結果存到new list，最後排序輸出。
# 如果答案是唯一，找到一組就停下來。

class Solution:
    def twoSum(self, nums, target):
        for Index, num in enumerate(nums):
            RESIDUE = target - nums[Index]
            if RESIDUE in nums:
                matchIndex = nums.index(RESIDUE)
                if matchIndex != Index:
                    Result = sorted([Index,matchIndex])
                    break
            else:
                continue
        return Result
        

S = Solution()

print(S.twoSum(testList,TARGET))

        

