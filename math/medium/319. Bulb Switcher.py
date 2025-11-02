import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        round 1 : 1 1 1 1 1 1 1 1 1 1       turn on all the lights
        round 2 : 1 0 1 0 1 0 1 0 1 0       turn off all the x % 2 == 0 
        round 3 : 1 0 0 0 1 1 1 0 0 0       turn off all the x % 3 == 9, 2 and 3 배수는 turn on
        round 4 : 1 0 0 1 1 1 1 1 0 0       turn on 4의 배수, still turn off if it is only 2의 배수
        round 5 : 1 0 0 1 0 1 1 1 0 1
        ...
        
        ith bulb
        6th bulb: toggle in 1,2,3,6 -> off

        count of factor should be odd number -> on
        but normally, the factor should be even number. 1 * 6, 2 * 3
        squares' factor should have odd number
        3*3

        so find the squares in n
        """
        return int(math.sqrt(n))