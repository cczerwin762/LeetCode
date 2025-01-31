'''
Prompt: 
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.
'''
def shortestAlternatingPaths(n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        if n <=1:
            return [0]*n
        ans = [-1] * n
        ans[0] =0
        blue = {}
        red = {}
        Q = []
        RBswitch = 2 #%2 = 0 -> red else blue 
        
        #put into dct where key = start nodes, val = end nodes
        for i in redEdges:
            if i[0] not in red:
                red[i[0]] = [i[1]]
            else:
                red[i[0]].append(i[1])
        for i in blueEdges:
            if i[0] not in blue:
                blue[i[0]] = [i[1]]
            else:
                blue[i[0]].append(i[1])

        #BFS starting red
        stepCount = 0
        rvisNodes = {}
        bvisNodes = {}
        if 0 in red:
            Q+=red[0]
            rvisNodes[0] = 1
            while Q:
                RBswitch +=1
                stepCount +=1
                neighbors = Q
                Q = []
                for neighbor in neighbors:
                    if RBswitch % 2 ==0:
                        if neighbor not in rvisNodes:
                            rvisNodes[neighbor] = 1
                            ans[neighbor] = min(ans[neighbor],stepCount) if ans[neighbor] !=-1 else stepCount
                            if neighbor in red :
                                Q+=red[neighbor]

                    else:
                        if neighbor not in bvisNodes:
                            bvisNodes[neighbor] = 1
                            ans[neighbor] = min(ans[neighbor],stepCount) if ans[neighbor] !=-1 else stepCount
                            if neighbor in blue:
                                Q+=blue[neighbor]

        stepCount = 0
        rvisNodes = {}
        bvisNodes = {}
        RBswitch = 1
        if 0 in blue:
            Q+=blue[0]
            bvisNodes[0] = 1
            while Q:
                RBswitch +=1
                stepCount +=1
                neighbors = Q
                Q = []
                for neighbor in neighbors:
                    if RBswitch % 2 ==0:
                        if neighbor not in rvisNodes:
                            rvisNodes[neighbor] =1
                            ans[neighbor] = min(ans[neighbor],stepCount) if ans[neighbor] !=-1 else stepCount
                            if neighbor in red :
                                Q+=red[neighbor]

                    else:
                        if neighbor not in bvisNodes:
                            bvisNodes[neighbor] = 1
                            ans[neighbor] = min(ans[neighbor],stepCount) if ans[neighbor] !=-1 else stepCount
                            if neighbor in blue:
                                Q+=blue[neighbor]
        
        return ans

if __name__ == "__main__":
    n = 5
    redEdges = [[3,2],[4,1],[1,4],[2,4]]
    blueEdges = [[2,3],[0,4],[4,3],[4,4],[4,0],[1,0]]
    print(shortestAlternatingPaths(n, redEdges, blueEdges))
