class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t=defaultdict(list)
        for i in strs:
            sor="".join(sorted(i))
            t[sor].append(i)
        return list(t.values())