class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            current=nums[i]
            wanted=target-current
            if wanted in seen:
                return [seen[wanted],i]

            seen[current]=i        

        
        
      

sol=Solution()
arr=[1,2,3,4,5]
target=7
ans=sol.twoSum(arr,target)
print(ans)
