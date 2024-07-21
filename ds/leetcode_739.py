class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0] * len(temperatures)
        stack=[]
        for i, val in enumerate(temperatures):
            # print("stack",stack)
            while stack and val > stack[-1][0]:
                print("stack",val,stack[-1])
                stackdata ,indx = stack.pop()
                print(indx,i,val)
                res[indx] = (i - indx)
            stack.append([val,i])
        return res

