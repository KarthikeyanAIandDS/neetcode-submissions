class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        l=0
        for num in s:
            if num-1 not in s:
                c=num
                le=1
                while c+1 in s:
                    c+=1
                    le+=1
                l=max(l,le)
            
        return l
