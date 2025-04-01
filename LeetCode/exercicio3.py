# 1929. Concatenation of Array

class Solution(object):
    def getConcatenation(self, nums):
        ans = nums[:] # Copia todos os elementos de nums para ANS
        ans += ans # Soma ANS + ANS
        return ans