class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if (2 <= len(nums) <= 10**4) and (-10**9 <= max(nums) <= 10**9) and (-10**9 <= target <= 10**9):
            num_indices = {}
            for i, num in enumerate(nums):
                complement = target - num
                if complement in num_indices:
                    return [num_indices[complement], i]
                num_indices[num] = i
            return []    
            