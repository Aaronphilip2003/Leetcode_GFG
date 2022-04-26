class Solution:
    def reverse(self, x: int) -> int:
        ostring = str(abs(x))[::-1]
    
        if int(ostring) > 2**(31):
            ostring = '0'
        
        elif x < 0:
            ostring = '-' + ostring
        
        return(int(ostring))
        
