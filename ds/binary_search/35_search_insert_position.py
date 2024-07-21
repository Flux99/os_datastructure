

## Floor


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # if target > nums[len(nums)-1]:
        #     return -1

        l,r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if target > nums[m]:
                l=m+1
            if target < nums[m]:
                r=m-1
        return l
        