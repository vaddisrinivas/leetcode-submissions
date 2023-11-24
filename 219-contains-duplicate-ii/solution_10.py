# https://leetcode.com/problems/contains-duplicate-ii
# https://leetcode.com/problems/219-contains-duplicate-ii
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        start, curr = 0,0
        s = dict()

        while curr < len(nums):
            # print(locals())
            if nums[curr] in s:
                if( curr-s[nums[curr]])<=k:
                    return True
                else:
                    start = curr
                    s.clear()
                    s[nums[curr]] = curr
            else:
                s[nums[curr]] = curr
            curr += 1
        return False

