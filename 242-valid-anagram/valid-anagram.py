class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counts={}
        for i in s:
            counts[i]=counts.get(i,0)+1
        for i in t:
            counts[i]=counts.get(i,0)-1
        for i in counts.values():
            if i!=0:
                return False
        return True
                