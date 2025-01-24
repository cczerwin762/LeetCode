'''
Prompt: 
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''
def main(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        tmp = []
        while i < m or j < n:
            if i >= m:
                tmp.append(nums2[j])
                j+=1
            elif j >= n:
                tmp.append(nums1[i])
                i+=1
            else:
                if nums1[i] < nums2[j]:
                    tmp.append(nums1[i])
                    i+=1
                elif  nums1[i] > nums2[j]:
                    tmp.append(nums2[j])
                    j+=1
                elif nums1[i]==nums2[j]: #equal
                    tmp.append(nums1[i])
                    tmp.append(nums2[j])
                    i+=1
                    j+=1

        for i in range(0,m+n):
            nums1[i] = tmp[i]

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    main(nums1, m, nums2, n)
    print(nums1)
