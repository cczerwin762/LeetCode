'''
Prompt:
Given a string s, find the length of the longest 
substring
without repeating characters.
'''
def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        dct = {}
        lowIdx = 0
        hiIdx = 0
        maxLength = 0
        for i in range(len(s)):
            if not s[i] in dct or dct[s[i]] < lowIdx:
                dct[s[i]] = i
                hiIdx = i
            else:
                lowIdx = dct[s[i]]+1
                dct[s[i]] = i
                hiIdx = i
            if hiIdx-lowIdx + 1 > maxLength:
                maxLength =  hiIdx-lowIdx + 1
            
            
        return maxLength
if __name__ == "__main__":
     s= 'pwwkewk'
     print(lengthOfLongestSubstring(s))