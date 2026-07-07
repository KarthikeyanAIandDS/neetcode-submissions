class Solution:

    def encode(self, strs: List[str]) -> str:
        r=[]
        for i in strs:
            r.append(str(len(i)))
            r.append('#')
            r.append(i)
        return "".join(r)

    def decode(self, s: str) -> List[str]:
        r=[]
        i=0
        while i< len(s):
            j=i
            while s[j]!='#':
                j+=1
            le=int(s[i:j])
            i=j+1
            j=i+le
            r.append(s[i:j])
            i=j
        return r
