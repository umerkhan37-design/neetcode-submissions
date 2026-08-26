class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for s in strs:
            count=[0]*26
            for i in s:
                 count[ord(i)-ord('a')]+=1
            
            ans[tuple(count)].append(s)


        return list(ans.values())



sol=Solution()


arr=["car", "rac", "tar", "rat", "fly", "lyf", "cook", "sook"]

print(sol.groupAnagrams(arr))        