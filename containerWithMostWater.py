'''
Prompt: 
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''
def maxArea( height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = -1
        maxArea = 0
        while i < len(height) and j >= -1*len(height):
            x = len(height)+j - i
            y = min(height[j],height[i])
            if x == 0:
                break
            if x*y > maxArea:
                maxArea = x*y
            if height[j] >= height[i]:
                i+=1
            elif height[i] > height[j]:
                j-=1
        return maxArea
        '''
        Solution 1: O(n^2)
        max = 0
        x = 0
        y = 0
        for i in range(0,len(height)):
            for j in range(0,len(height)):
                x = abs(j-i)
                y = min(height[i],height[j])
                if x*y > max:
                    max = x*y
        return max
        '''
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))