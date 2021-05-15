#THIS WAS ONLY FASTER THAN 5% OF THE SOLUTIONS, LOL! 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add = int(a , 2) + int(b , 2)
        return bin(add)[2:]

    
#WHEREAS IF I DO THIS, IT MAKES IT FASTER THAN 97% OF THE SOLUTION...LIKE WTF!
class Solution:
def addBinary(self, a: str, b: str) -> str:
    tot = int(a, 2) + int(b, 2)
    return bin(tot).replace("0b", "")
