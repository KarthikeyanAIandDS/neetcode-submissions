class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t=defaultdict(list)
        
        for i in strs:
            h=[0]*26
            for c in i:
                h[ord(c)-ord('a')]+=1
            t[tuple(h)].append(i)
        return list(t.values())
            

            