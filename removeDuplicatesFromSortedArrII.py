'''
Prompt: 
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''
def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        k = 0
        while i < len(nums):
            dupCheck = False
            greaterExists = False
            k+=1
            j = i+1
            while j< len(nums):
                if nums[i]==nums[j]:
                    dupCheck = True
                if nums[j] > nums[i]:
                    greaterExists = True
                    break #saves j as index of new hi number
                j+=1
            if not greaterExists:
                if dupCheck:
                    k+=1 # need to check for dups before we jump out
                    nums[i+1] = nums[i] # backfill
                break #we're done nothing greater exists in the array
            if dupCheck: 
                # swap 
                # dup exists at i+1 (if it doesn't we need to put it there)
                k+=1 # for the duplicate
                tmp = nums[i+2]
                nums[i+1] = nums[i] #backfill
                nums[i+2] = nums[j]
                nums[j] = tmp
                i = i+2
            else:
                # no dup exists
                tmp = nums[i+1]
                nums[i+1] = nums[j]
                nums[j] = tmp
                i = i+1
        return k

if __name__ == "__main__":
    nums = [1,1,1,1,2,2,3,3,3]
    k = removeDuplicates(nums)
    print(nums[:k])