

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        if n > len(s2):
            return False

        target = Counter(s1)

        for i in range(len(s2) - n + 1):
            window = s2[i:i + n]

            if Counter(window) == target:
                return True

        return False
            
            
                
                    


                
            





        