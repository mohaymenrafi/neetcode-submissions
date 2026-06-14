class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        if len(nums) == 0 or len(nums) == 1:
            return False
        store = {}
        for num in nums:
            if num in store:
                return True
            else:
                store[num] = num
        return False