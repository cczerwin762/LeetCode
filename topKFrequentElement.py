import heapq
'''
Prompt:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dct = {}
        for i in nums:
            if i in dct:
                dct[i] +=1
            else:
                dct[i] = 1

        tcd = {}
        for key in dct:
            if dct[key] not in tcd:
                tcd[dct[key]] = [key]
            else:
                tcd[dct[key]].append(key)

        minHeap = []
        lenHeap = 0
        for key in tcd:
            heapq.heappush(minHeap,key) #put frequencies in a minHeap
            lenHeap+= len(tcd[key])
            while lenHeap > k:
                tmp = heapq.heappop(minHeap)
                lenHeap-=len(tcd[tmp])
        ans = []
        for i in minHeap:
            ans += tcd[i]
        return ans

if __name__ == "__main__":
    x = [3,3,3,5,5,5,1,1,2]
    print(topKFrequent(x,2))
