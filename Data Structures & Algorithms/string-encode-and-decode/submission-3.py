class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str=""
        for i in strs:
            length=str(len(i))
            new_str += length + "#" + i
        return new_str


    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            string=s[j+1:length+1+j]
            res.append(string)
            i=j+1+length
        return res
