class Solution(object):
    def numIdenticalPairs(self, nums):
        sum = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] == nums[j]):
                    sum = sum + 1
        return sum
