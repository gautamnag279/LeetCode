#THIS IS GIVING VALUE ERROR
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(str(n)[::-1] , 2)
        
#SO INSTEAD
class Solution:
    def reverseBits(self, n: int) -> int:
        return int('{0:032b}'.format(n)[::-1] , 2
                   
