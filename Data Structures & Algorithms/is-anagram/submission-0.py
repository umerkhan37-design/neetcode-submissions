class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        if sorted(s)==sorted(t):
             return True  

        else:
             return False      
        


sol=Solution()

word1="racecar"
word2="carrace"
ans=sol.isAnagram(word1, word2)
print(ans)