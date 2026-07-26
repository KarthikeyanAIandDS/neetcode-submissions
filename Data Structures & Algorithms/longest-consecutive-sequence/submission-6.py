class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        for i in s:
            if i-1 not in s:
                c=i
                length=1
                while c+1 in s:
                    c+=1
                    length+=1
                longest=max(longest,length)
        return longest
