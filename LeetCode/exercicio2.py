## 2769. Find the Maximum Achievable Number

class Solution(object):
    def theMaximumAchievableX(self, num, t):
       x = num + 2 * t # A cada operação, x pode aumentar 2 vezes o número de operações permitidas (t)
       return x