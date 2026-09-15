class Solution:

    def encode(self, strs: List[str]) -> str:
        words=""
        for word in strs:
            length=str(len(word))
            words=words+'#'+length+'#'+word
        return words

    def decode(self, s: str) -> List[str]:
        arr=[]
        length=len(s)-1
        word_len=0
        start=0
        end=0
        i=0
        while i<=length:
                if s[i]=="#":
                    start=i+1
                end=s.find('#', start)
                print(s[start:end])
                word_len=int(s[start:end])
                arr.append(s[end+1:word_len+end+1])
                i=word_len+end+1
        return arr



