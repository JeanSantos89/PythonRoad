# 1108. Defanging an IP Address

class Solution(object):
    def defangIPaddr(self, address):
        NewAddress = [] # Cria nova lista
        for i in address: # Percorre lista Address
            if i == '.': # Se achar . na Lista
                NewAddress.append("[.]") # Adiciona [.]
            else: # Se não
                NewAddress.append(i) # Adiciona o elemento ao fim da lista
        return "".join(NewAddress) # Retorna a nova lista sem espaçamento
        