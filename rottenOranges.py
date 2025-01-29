'''
Prompt: 
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''
def orangesRotting(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        totalOrangeCount = 0
        rottenOrangeCount = 0

        queue = []
        minute = 0
        m = len(grid) #numRows
        n = len(grid[0])#numCols

        #loop through to get oranges
        for row in range(m):
            for col in range(n):
                if grid[row][col]==2:
                    queue.append(row*n + col)
                    rottenOrangeCount +=1
                    totalOrangeCount +=1
                elif grid[row][col] ==1:
                    totalOrangeCount +=1

        while queue:
            
            tmpQ = queue
            queue = []
            #for neighbors in tmpQ that ==1 change to 2 and add to queue
            for i in tmpQ:
                #go up down left and right and check ==1 
                #grid[r][c] ==2 
                r = i//n
                c = i%n
                #up
                if r-1 > -1 and grid[r-1][c] ==1:
                    grid[r-1][c] =2
                    rottenOrangeCount+=1
                    queue.append((r-1)*n+c)
                #down
                if r+1 < m and grid[r+1][c] ==1:
                    grid[r+1][c] =2
                    rottenOrangeCount+=1
                    queue.append((r+1)*n+c)
                #left
                if c-1 > -1 and grid[r][c-1] ==1:
                    grid[r][c-1] =2
                    rottenOrangeCount+=1
                    queue.append((r)*n+(c-1))
                #right
                if c+1 < n and grid[r][c+1] ==1:
                    grid[r][c+1] =2
                    rottenOrangeCount+=1
                    queue.append((r)*n+(c+1))

            minute+=1
        
        if minute:
            minute-=1

        return minute if totalOrangeCount == rottenOrangeCount else -1


if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(orangesRotting(grid))