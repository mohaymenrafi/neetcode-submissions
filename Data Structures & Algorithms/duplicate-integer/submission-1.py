class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for num in nums:
            if num in store:
                return True
            store[num] = 0
        return False
        