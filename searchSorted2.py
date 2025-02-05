'''
Prompt: 
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
'''
def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums)-1
        while r >= l:
            m = ((r-l)//2) + l
            if nums[m] == target:
                return True
            if nums[l]  < nums[m]: #this part is sorted
                if nums[l] == target:
                    return True
                if nums[l] < target < nums[m]:
                    r = m-1
                else: 
                    l = m+1
            elif nums[l] == nums[m]: #pivot exists somewhere between or all the same
                l+=1
            else: #this part is sorted
                if nums[r] == target:
                    return True
                if nums[r] > target > nums[m]:
                    l = m+1
                else:
                    r = m-1
        return False

if __name__ == "__main__":
    print('hello world')