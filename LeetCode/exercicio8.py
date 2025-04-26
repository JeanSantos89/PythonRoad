# 1512. Number of Good Pairs

class Solution(object):
    def numIdenticalPairs(self, nums):
        pares = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == (nums[j]) and i<j:
                    pares+= 1
                else:
                    continue
        return pares

        