class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        result=r
        while l<=r:
            k=(l+r)//2
            times=0
            for p in piles:
                times+=math.ceil(float(p)/k)
            if times<=h:
                result=k
                r=k-1
            else:
                l=k+1
        return result
      