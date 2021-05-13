class Solution:
    def runTest(self,l,r,s,result):
        while l>=0 and r<len(s) and s[l] == s[r]:
            if (r+1-l) > len(result):
                result = s[l:r+1]
            l -= 1
            r += 1
        return result
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            result = self.runTest(i,i,s,result)
            result = self.runTest(i,i+1,s,result)
        return result
