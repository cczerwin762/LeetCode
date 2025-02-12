'''
Prompt: 
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''

def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k ==0 or len(nums) <=1:
            return nums
        stack = []
        i = 0
        while i < len(nums):
            if len(stack) < k:
                stack.append(nums[(k+i)%len(nums)])
                nums[(k+i)%len(nums)] = nums[i]
                nums[i] = None
            else:
                tmp = nums[(k+i)%len(nums)]
                nums[(k+i)%len(nums)] = stack.pop(0)
                stack.append(tmp)
            i+=1
        return nums

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(rotate(nums,k))
