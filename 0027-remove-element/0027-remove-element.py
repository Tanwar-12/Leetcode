class Solution(object):
    def removeElement(self, nums, val):
        low = -1
        high = len(nums)
        while low < high:
            if len(nums) == 0:
                return len(nums)
            if len(nums) == 1:
                if nums[low] == val:
                    return 0
                else: 
                    return 1
            low = low + 1
            high = high - 1
            if nums[low] == val:
                del[nums[low]]
                low -= 1
                high -= 1
            if nums[high] == val:
                del[nums[high]]
        return len(nums)
        
        