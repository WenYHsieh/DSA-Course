class Solution():
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums or len(nums)<4:
            return
        
        stack = []
        nums.sort()
        
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i] * 4  > target:
                break
                
            for j in range (i+1, len(nums)-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[j] * 3 > target-nums[i]:
                    break
                
                low = j+1
                high = len(nums)-1
                while low < high:
                    data = (nums[i] + nums[j] + nums[low] + nums[high])
                    if data == target:
                        stack.append([nums[i], nums[j], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low+1]:
                            low+=1
                        while low < high and nums[high] == nums[high-1]:
                            high-=1
                        low +=1
                        high -=1
                    elif (nums[i] + nums[j] + nums[low] + nums[high]) < target:
                        low +=1
                    else:
                        high -=1
        return stack

nums = list(range(-3,100000))

target = 0
print(Solution().fourSum(nums, target))