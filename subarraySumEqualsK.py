'''
Prompt:
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
'''

def subarraySum(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # prefix sum array 
        # sum of sub arrays = nums[j] - nums[i-1]
        # count = sub array count
        sumCount = 0
        for i in range(1,len(nums)):
            nums[i] += nums[i-1] # make prefix sum
        count = {0:1}
        for i in range(0,len(nums)):
            if (nums[i]-k) in count:
                sumCount+= count[nums[i]-k]
            if nums[i] in count:
                count[nums[i]]+=1
            else:
                count[nums[i]] = 1

        '''
        Solution 1
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if i==0:
                    if nums[j] - 0 == k:
                        count+=1
                else:
                    if nums[j] - nums[i-1] == k:
                        count+=1
        '''
        return sumCount

if __name__ == "__main__":
     nums = [1,2,3,4,-1,2,7,-6,8,1]
     k = 3
     print(subarraySum(nums,k))