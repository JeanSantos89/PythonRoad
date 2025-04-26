# 771. Jewels and Stones

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        contagem = 0
        for i in range(len(stones)):
            for x in range(len(jewels)):
                if jewels[x] in stones[i]:
                    contagem += 1
                else:
                    continue
        return contagem

        