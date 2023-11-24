# https://leetcode.com/problems/asteroid-collision
# https://leetcode.com/problems/735-asteroid-collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i, item in enumerate(asteroids):
            # print(locals())
            if item>0:
                st = [item]+st
            else:
                if st==[] or st[0]<0:
                    st = [item]+st
                    continue
                while st:
                    if st[0]<0:
                        st = [item]+st
                        break
                    if st[0]==abs(item):
                        st = st[1:]
                        break
                    elif st[0]<abs(item):
                        st = st[1:]
                    else:
                        break
                else:
                    st = [item]
        return st[::-1]