# https://leetcode.com/problems/reverse-bits
# https://leetcode.com/problems/190-reverse-bits
class Solution:
    def reverseBits(self, n: int) -> int:
        n = list(bin(n))[2:]
        l = len(n)
        print(l)
        exn = ['0']*(32-l)
        exn.extend(n)
        n = exn
        l = len(n)
        print(l)

        for i in range((l//2)):
            print(n[i],n[l-1-i])
            n[i],n[l-1-i]=n[l-1-i],n[i]
            
        print("".join(n))
        return int("".join(n),2)

        