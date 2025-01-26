'''
Prompt:
You are given a 2D integer array ranges where ranges[i] = [starti, endi] denotes that all integers between starti and endi (both inclusive) are contained in the ith range.

You are to split ranges into two (possibly empty) groups such that:

Each range belongs to exactly one group.
Any two overlapping ranges must belong to the same group.
Two ranges are said to be overlapping if there exists at least one integer that is present in both ranges.

For example, [1, 3] and [2, 5] are overlapping because 2 and 3 occur in both ranges.
Return the total number of ways to split ranges into two groups. Since the answer may be very large, return it modulo 109 + 7.
'''
def countWays(ranges):
        """
        :type ranges: List[List[int]]
        :rtype: int
        """
        merged = []
        ranges = sorted(ranges)
        for i in range(0,len(ranges)):
            if i == 0:
                merged.append(ranges[i])
            else:
                if ranges[i][0] <= merged[-1][1]:
                    merged[-1][1] = max(ranges[i][1],merged[-1][1])
                else:
                    merged.append(ranges[i])
        return 2**len(merged) %(10**9 +7)


if __name__ == "__main__":
     print(countWays([[1,6],[2,3],[2,9],[10,15],[12,20],[50,100]]))
