#1920. Build Array from Permutation

class Solution(object):
    def buildArray(self, nums):
        ans = [0] * len(nums) #Cria uma lista com o tamanho de Nums 
        for i in range(len(nums)): # i irá percorrer o tamanho de nums
            ans[i] = nums[nums[i]] # com a fórmula, iremos acessar o valor do indíce [0,2,1,5,3,4] - no índice 3, pegamos o valor 5 e procurar a posição 5 do array = 4.
        return ans
    


"""
class Solution(object):
    def buildArray(self, nums):
        ans = []  Se eu definir a lista apenas como vazia, ela será necessário ter append para inserir um por um
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
"""