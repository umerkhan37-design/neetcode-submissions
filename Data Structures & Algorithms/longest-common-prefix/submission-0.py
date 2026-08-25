class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
     if not strs:
         return ""
     strs.sort()
     first=strs[0]
     sec=strs[-1]
     ans =""
     for i in range(min(len(first), len(sec))):
        if first[i]==sec[i]:
            ans+=first[i]
        else:
            return ans
     return ans            

sol=Solution()
strs=["cat","car","came","call","cace"]
ans=sol.longestCommonPrefix(strs)
print(ans)
        