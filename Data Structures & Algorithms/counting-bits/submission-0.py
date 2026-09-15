class Solution:
    def countBits(self, n: int) -> List[int]:
        number=0
        binary=[]
        result=[]
        for i in range(n+1):
            number=i
            binary.append(number)
        for i in binary:
            number=i
            sum=0
            while number:
                number&=number-1
                sum+=1
            result.append(sum)
        return result
