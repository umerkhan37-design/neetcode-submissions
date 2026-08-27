class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        register={}
        half=len(nums)/2

        for n in nums:
            register[n]=register.get(n, 0)+1
            if register[n]>half:
                 return n






sol=Solution()

nums=[1,1,1,2,3,4,4,5,5,5,5,5]
print(sol.majorityElement)        
        