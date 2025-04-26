# 771. Jewels and Stones

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        contagem = 0
        for i in range(len(stones)):
            if stones[i] in jewels:
                contagem += 1
        return contagem        