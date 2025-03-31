# Questão: 3110. Score of a string

class Solution(object):
    def scoreOfString(self, s): # Passagem de função
        calc = 0 # Define a pontuação inicial como 0
        for i in range(len(s)-1): # Percorre a string 
            calc += abs(ord(s[i]) - ord(s[i+1])) # Em cada repetição, ira resultar e somar: valor absoluto e valor ASCII de index [0 - 1] e [1-2] e [2-3].... até a somatória final.
        return calc # Retorna a soma total das diferenças
