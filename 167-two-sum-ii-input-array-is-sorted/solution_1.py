# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# https://leetcode.com/problems/167-two-sum-ii-input-array-is-sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j,l = 0,len(numbers)-1,len(numbers)
        if l==2: return [1,2] if sum(numbers)==target else []
        while i<l and j>-1:
            if j>0 and numbers[j]>target:
                j-=1
                continue
            t = numbers[i]+numbers[j]
            # print(i,j,t)
            if t<target:
                i+=1
                continue
            elif t>target:
                j-=1
            else:
                if i<j:
                    return [i+1,j+1] 
                elif j<i:
                    return [j+1,i+1]
                else:
                    return [i+1,i+2]
            