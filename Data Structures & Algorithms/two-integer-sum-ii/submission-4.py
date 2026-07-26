class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=0
        r=len(numbers)-1
        while n<r:
            s=numbers[n]+numbers[r]
            if s == target:
                return [n+1,r+1]
            elif s < target:
                n+=1
            else:
                r-=1
        
