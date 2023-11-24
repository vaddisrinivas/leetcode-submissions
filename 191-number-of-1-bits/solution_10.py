# https://leetcode.com/problems/number-of-1-bits
# https://leetcode.com/problems/191-number-of-1-bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        return list(bin(n)).count("1")