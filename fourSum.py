class Solution():
    def fourSum(self, nums, target):  
        nums.sort()   
        numsLength = len(nums)   
        Result = []
        
        for index1 in range(numsLength):
            if index1>0 and nums[index1] == nums[index1-1]:
                continue
            if nums[index1]*4 > target:
                break
                
            for index2 in range (index1+1, numsLength):
                if index2>index1+1 and nums[index2] == nums[index2-1]:
                    continue
                if nums[index2]*3 > target-nums[index1]:
                    break
                # 2 pinter
                lowIndex = index2+1
                highIndex = len(nums)-1

                while lowIndex < highIndex:
                    fourNumSum = nums[index1] + nums[index2] + nums[lowIndex] + nums[highIndex]
                    if fourNumSum < target:
                        lowIndex+=1
                    elif fourNumSum > target: 
                        highIndex-=1
                    else:
                        tmp = sorted([nums[index1], nums[index2], nums[lowIndex], nums[highIndex]])
                        Result.append(tmp)
                        
                        while lowIndex < highIndex and nums[lowIndex] == nums[lowIndex+1]: 
                            lowIndex+=1
                        while lowIndex < highIndex and nums[highIndex] == nums[highIndex-1]:
                            highIndex-=1
                        lowIndex+=1
                        highIndex-=1

        return Result

nums = [1, 0, -1, -2, 2]
target = 0
print(Solution().fourSum(nums, target))