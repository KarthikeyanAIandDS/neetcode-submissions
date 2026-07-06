class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        fr=[[] for i in range(len(nums)+1)]
        for num in nums:
            c[num]=1+c.get(num,0)
        for n,c in c.items():
            fr[c].append(n)
        r=[]
        for i in range(len(fr)-1,0,-1):
            for n in fr[i]:
                r.append(n)
                if len(r)==k:
                    return r