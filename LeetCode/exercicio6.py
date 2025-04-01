#2161. Partition Array According to Given Pivot
class Solution(object):
    def pivotArray(self, nums, pivot):
        menor = []
        maior = []
        igual = []

        for i in nums: # Estou percorrendo os VALORES do array
            if i < pivot:
                menor.append(i)
            elif i > pivot:
                maior.append(i)
            elif i == pivot:
                igual.append(i)
        
        return menor + igual + maior # Retorno o montante das listas
        

        """
        class Solution(object):
            def pivotArray(self, nums, pivot):
                menor = []
                maior = []
                igual = []

                for i in range(len(nums)): #Aqui estou percorrendo os index do array
                    if nums[i] < pivot:
                        menor.append(i)
                    elif nums[i] > pivot:
                        maior.append(i)
                    elif nums[i] == pivot:
                        igual.append(i)
                
                return menor + igual + maior # O montante seria apenas os index - 0,1,2,3 ao invés dos valores
        """