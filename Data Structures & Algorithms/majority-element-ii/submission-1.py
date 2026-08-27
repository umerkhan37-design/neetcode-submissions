class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        register={}
        half=len(nums)/3
        result=[]
        for n in nums:
            register[n]=register.get(n, 0)+1

        for k in register:
           if register[k]>half:
            result.append(k)
                      

        return result




sol=Solution
arr=[1,2,2,2,2,2,77,77,77,77,77,77,77,77]
print(sol.majorityElement)
        