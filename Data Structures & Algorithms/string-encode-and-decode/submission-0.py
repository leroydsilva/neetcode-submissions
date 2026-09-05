class Solution:

    def encode(self, strs: List[str]) -> str:
        delimeter="#"
        enco=""
        for word in strs:
            leng=str(len(word))
            enco+=leng+delimeter+word
        return enco

    def decode(self, s: str) -> List[str]:
        delimeter="#"
        res=[]
        i=0
        while i < len(s):
            j=s.find(delimeter,i)
            var=int(s[i:j])
            word=s[j+1:j+var+1]
            res.append(word)
            i=j+var+1
        return res
            
