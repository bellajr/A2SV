#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_pair = dict()
        
        for i in range(len(nums)):
            if nums[i] in val_pair:
                return [val_pair[nums[i]], i]
            
            else:
                val_pair[target - nums[i]] = i
# @lc code=end

