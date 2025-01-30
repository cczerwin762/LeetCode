'''
Prompt: 
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.
'''

def lengthOfLIS(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        dp = [nums,[1]*len(nums)]
        maxK = 1
        i = len(nums)-2
        
        while i >= 0:
            localMax = 1
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    localMax = max(dp[1][j] +1,localMax)
            dp[1][i] = localMax
            maxK = max(maxK,localMax)
            i-=1
        return maxK

if __name__ == "__main__":
     nums = [0,1,0,3,2,3]
     print(lengthOfLIS(nums))