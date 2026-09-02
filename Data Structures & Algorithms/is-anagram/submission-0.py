class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for str1 in s:
            if str1 in d1:
                d1[str1]+=1
            else:
                d1[str1]=1
        for str2 in t:
            if str2 in d2:
                d2[str2]+=1
            else:
                d2[str2]=1
        return d1 == d2
