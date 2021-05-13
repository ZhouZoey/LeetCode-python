# 方法一：贪心算法 总是找局部最优
digits = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
          (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
          (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

class Solution(object):
    def intToRoman(self, num: int) -> str:
        roman_digits = []
        for value, symbol in digits:
            if num == 0:
                break
            count, num = divmod(num, value)
            roman_digits.append(symbol * count)
        return "".join(roman_digits)

if __name__ == '__main__':
    num = 1984
    s = Solution()
    print(s.intToRoman(num))