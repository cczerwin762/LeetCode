'''
Prompt: 
Given a string s, return the longest 
palindromic
 
substring
 in s.
'''


def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <=1:
            return s
        i = 0
        maxPalindrome = ""
        while i < len(s):
            i2 = i
            j2 = len(s)-1
            j = i
            while j2 > i2:
                if s[i2] == s[j2]:
                    j = max(j2,j)
                    i2+=1
                    j2-=1
                else:
                    j2 = j2-1 if i2==i else j-1
                    j = i
                    i2 = i
            maxPalindrome = s[i:j+1] if len(s[i:j+1]) > len(maxPalindrome) else maxPalindrome
            i+=1
        return maxPalindrome

if __name__ == "__main__":
     s = "xxxyzzyxxxx"
     print(longestPalindrome(s))