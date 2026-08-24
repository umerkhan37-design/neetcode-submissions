class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False

sol = Solution()
nums = [1, 2, 3, 1]
answer = sol.hasDuplicate(nums)
answer = sol.hasDuplicate(nums)

