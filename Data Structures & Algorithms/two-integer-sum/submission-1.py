class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p={}
        for i,n in enumerate(nums):
            di=target-n
            if di in p:
                return [p[di],i]
            p[n]=i