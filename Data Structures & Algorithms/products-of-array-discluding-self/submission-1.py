class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        p=1
        for i in range(len(nums)):
            res[i]=p
            p*=nums[i]
        po=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=po
            po*=nums[i]
        return res