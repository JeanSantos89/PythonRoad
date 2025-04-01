#2469. Convert the Temperature

class Solution(object):
    def convertTemperature(self, celsius):
        escalas = []
        if celsius is not None:
            escalas.append(celsius + 273.15)
            escalas.append(celsius * 1.8 + 32.00)
        return escalas
        