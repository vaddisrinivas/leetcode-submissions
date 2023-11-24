# https://leetcode.com/problems/max-number-of-k-sum-pairs
# https://leetcode.com/problems/1798-max-number-of-k-sum-pairs
# from pprint import pprint
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # comps = [abs(k-i) for i in nums]
        dict_nums = {}
        for i in nums:
            if i in dict_nums:
                dict_nums[i]+=1
            else:
                dict_nums[i]=1
        i = 0
        j = 0
        # print(dict_nums)
        while i<len(nums):
            # pprint(locals())
            if dict_nums[nums[i]]>0:
                dict_nums[nums[i]] -= 1
            else:
                i+=1
                continue
            if k-nums[i] in dict_nums and dict_nums[k-nums[i]]>0:
                dict_nums[k-nums[i]] -= 1
                j += 1
            else:
                dict_nums[nums[i]] += 1
            i += 1
        return j

