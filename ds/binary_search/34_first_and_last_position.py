class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]

        ans[0]= self.searchocurrence(nums,target,True)
        ans[1]= self.searchocurrence(nums,target,False)
        return ans


    
    def searchocurrence(self,nums:List[int],target,firstposition:bool)-> int:
        ans = -1
        l,r= 0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target < nums[m]:
                r=m-1
            elif target > nums[m]:
                l=m+1
            else:
                ans=m
                if firstposition:
                    r=m-1
                else:
                    l=m+1
        return ans





        