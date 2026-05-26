class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const store = {}
        for (const num of nums){
            if(store[num]) {
                return true
            }
            store[num] = 1
        }
        return false
    }
}
