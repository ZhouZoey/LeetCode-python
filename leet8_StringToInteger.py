INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

# 方法一： 正常遍历
class Solution1(object):
    def myAtoi(self, str1: str) -> int:
        i = 0
        n = len(str1)
        while i < n and str1[i] == ' ':
            i += 1
        if n == 0 or i == n:
            return 0
        flag = 1
        if str1[i] == '-':
            flag = -1
        if str1[i] == '+' or str1[i] == '-':
            i += 1
        ans = 0
        while i < n and '0' <= str1[i] <= '9':
            ans = ans * 10 + int(str1[i]) - int('0')
            i += 1
            if ans - 1 > INT_MAX:
                break
        ans *= flag
        if ans > INT_MAX:
            return INT_MAX
        return INT_MIN if ans < INT_MIN else ans

#方法二： 有限状态机
class Automaton(object):
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0

        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed':['end','end','in_number', 'end'],
            'in_number':['end', 'end', 'in_number', 'end'],
            'end':['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

class Solution2(object):
    def myAtoi(self, str1: str) -> int:
        automation = Automaton()
        for c in str1:
            automation.get(c)
        value = automation.sign * automation.ans
        if value > INT_MAX:
           return INT_MAX
        return INT_MIN if value < INT_MIN else value

# 方法三： 正则表达式
class Solution3(object):
    def myAtoi(self, str1 : str) -> int:
        import re
        mathes = re.match('[]*([+-]?\d+)', str1)
        if not mathes:
            return 0
        ans = int(mathes.group(1))
        return min(max(ans, -2 ** 31), 2 ** 31 - 1)

if __name__ == '__main__':
    s = ' -42'
    a = Solution2()
    print(a.myAtoi(s))
