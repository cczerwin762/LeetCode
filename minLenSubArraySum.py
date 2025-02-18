'''
Prompt: 
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
'''

def minSubArrayLen(target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = 0
        minLen = len(nums) +1
        curSum = 0
        while hi < len(nums) or (curSum >= target):
            if curSum < target:
                curSum+=nums[hi]
                hi+=1
            else:
                minLen = min(minLen, hi-lo)
                curSum-=nums[lo]
                lo+=1
                if lo >= len(nums):
                    break
        return 0 if minLen > len(nums) else minLen

if __name__ == "__main__":
     nums = [1,2,3,4,5,6,7]
     print(minSubArrayLen(7, nums))
