class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top,bot= 0, rows-1
        while top <= bot:
            mid = (top+bot)//2
            if target > matrix[mid][-1]:
                top= mid+1
            elif target < matrix[mid][0]:
                bot = mid-1
            else:
                break
        if not (top <= bot):
            return False
        l,r = 0,cols-1
        mid = (top+bot)//2
        while l <=r:
            m = (l+r)//2
            if matrix[mid][m] < target:
                l=m +1
            elif matrix[mid][m] > target:
                r=m -1
            else:
                return True
        return False

        
        

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 0,max(piles)
        res = r

        while l <= r:
            mid = (l+r)//2
            hours=0
            for p in piles:
                hours+=(p/mid)
            if hours <=h:
                res=min(res,hours)
                r=mid-1
            else:
                l=mid+1
        return res
