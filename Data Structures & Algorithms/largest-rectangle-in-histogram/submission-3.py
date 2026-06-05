class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxa=0
        n=len(heights)
        for i,height in enumerate(heights):
            start=i
            while stack and height<stack[-1][0]:
                h,j=stack.pop()
                w=i-j
                a=h*w
                maxa=max(maxa,a)
                start=j
            stack.append((height,start))
        while stack:
            h,j=stack.pop()
            w=n-j
            maxa=max(maxa,h*w)
        return maxa
