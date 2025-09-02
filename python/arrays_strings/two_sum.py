'''
Given an array of integers nums and an integer target
return which indices of the two numbers such that they add up to 
the target
'''

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        '''Start function two_sum'''
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
        return [] # No solution found


solution = Solution()
nums = [1,2,5,7,9]
target = 12
print(solution.two_sum(nums, target))
