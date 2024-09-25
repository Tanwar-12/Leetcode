class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        if not (2 <= len(nums) <= 10**4 and all(-10**9 <= num <= 10**9 for num in nums) and -10**9 <= target <= 10**9):
            raise ValueError("Input values do not satisfy constraints.")        
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return None
        