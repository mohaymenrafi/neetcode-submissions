class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store = {}
        for num in nums:
            store[num] = store.get(num, 0) + 1
        return max(store, key=store.get)
    
        