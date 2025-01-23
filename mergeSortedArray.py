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
