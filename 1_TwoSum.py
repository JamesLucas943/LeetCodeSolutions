class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i, len(nums)-1):
                if(nums[i]+nums[j+1] == target):return [i,j+1]
