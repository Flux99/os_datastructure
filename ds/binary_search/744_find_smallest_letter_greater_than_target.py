class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,r = 0, len(letters)-1
        while l <= r:
            m = (l+r)//2
            if target < letters[m]:
                r=m-1
            else:
                l=m+1
            
        return letters[l% len(letters)]
        