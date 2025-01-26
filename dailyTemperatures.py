'''
Prompt:
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
def dailyTemperatures( temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                numDays = i-stack[-1]
                answer[stack.pop(-1)] = numDays
            stack.append(i)
        return answer
        '''
        sol1
        for i in range(0,len(temperatures)):
            count = 1
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    answer[i] = count
                    break
                else: 
                    count+=1
        return answer
        '''

if __name__ == "__main__":
     print(dailyTemperatures([73,73,75,71,69,72]))