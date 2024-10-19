class Solution:
    def rev_inv(self, s: str) -> str:
        return ''.join('1' if char == '0' else '0' for char in s[::-1])

    def gen_string(self, n: int) -> str:
        s = "0" 
        i = 1
        while i < n:
            s = s + "1" + self.rev_inv(s)
            i += 1
        return s

    def findKthBit(self, n: int, k: int) -> str:
        s = self.gen_string(n)
        return s[k - 1] 
