'''
Prompt: 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans =[]
        if len(nums) < 3:
            return ans
        nums = sorted(nums)
        for i in range(len(nums)): 
            if i > 0 and nums[i]  == nums[i-1]:
                continue
            j = i+1
            k = len(nums) -1
            while j < k:
                sm = nums[i] + nums[j] + nums[k]
                if sm ==0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                    while nums[k] == nums[k+1] and j < k:
                        k-=1
                elif sm > 0:
                    k-=1
                else:
                    j+=1
                    
        return ans

if __name__ == "__main__":
    nums = [-4,-1,-1,0,1,2]
    print(threeSum(nums))