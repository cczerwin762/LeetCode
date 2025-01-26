'''
Prompt:

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