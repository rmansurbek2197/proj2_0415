# 1
class SumN:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return sum(range(1, self.n + 1))

n = int(input())
print(SumN(n).solve())

# 2
class EvenCheck:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return self.n % 2 == 0

n = int(input())
print(EvenCheck(n).solve())

# 3
class DigitCount:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return len(str(self.n))

n = int(input())
print(DigitCount(n).solve())

# 4
class MaxTwo:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def solve(self):
        return max(self.a, self.b)

a, b = map(int, input().split())
print(MaxTwo(a, b).solve())

# 5
class DigitSum:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return sum(map(int, str(self.n)))

n = int(input())
print(DigitSum(n).solve())
